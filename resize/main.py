import os
from PIL import Image


def resize_images(folder_path, input_types=None, small_width=320, medium_width=640):
    """
    Thay đổi kích thước ảnh từ thư mục được chỉ định thành kích thước nhỏ và trung bình trong khi duy trì tỷ lệ khung hình.
    Lưu ảnh đã thay đổi kích thước với hậu tố "-small" và "-medium" trong tên tệp.

    Tham số:
        folder_path (str): Đường dẫn tới thư mục chứa các ảnh.
        input_types (list, optional): Danh sách phần mở rộng tệp ảnh cần xử lý. Mặc định là tất cả ảnh nếu là None hoặc để trống.
        small_width (int): Chiều rộng mục tiêu cho ảnh kích thước nhỏ.
        medium_width (int): Chiều rộng mục tiêu cho ảnh kích thước trung bình.
    """
    # Default extensions if input_types is None or empty
    if input_types is None or len(input_types) == 0:
        input_types = []  # Empty list means process all files regardless of type
    else:
        # Add "." before each extension if input_types is not blank
        input_types = [f".{ext.strip().lower()}" for ext in input_types]

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        file_extension = os.path.splitext(filename)[1].lower()

        # If input_types is empty, process all files; otherwise, check if the file matches extensions
        if os.path.isfile(file_path) and (len(input_types) == 0 or file_extension in input_types):
            try:
                with Image.open(file_path) as img:
                    # Get original dimensions
                    original_width, original_height = img.size

                    # Calculate height for small size while maintaining aspect ratio
                    small_height = int((small_width / original_width) * original_height)
                    small_resized = img.resize((small_width, small_height), Image.Resampling.LANCZOS)
                    small_file_name = f"{os.path.splitext(filename)[0]}-small{file_extension}"
                    small_save_path = os.path.join(folder_path, small_file_name)
                    small_resized.save(small_save_path)
                    print(f"Saved: {small_save_path}")

                    # Calculate height for medium size while maintaining aspect ratio
                    medium_height = int((medium_width / original_width) * original_height)
                    medium_resized = img.resize((medium_width, medium_height), Image.Resampling.LANCZOS)
                    medium_file_name = f"{os.path.splitext(filename)[0]}-medium{file_extension}"
                    medium_save_path = os.path.join(folder_path, medium_file_name)
                    medium_resized.save(medium_save_path)
                    print(f"Saved: {medium_save_path}")

            except Exception as e:
                print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    folder_path = input("Nhập đường dẫn thư mục chứa ảnh: ").strip()
    input_types_raw = input(
        "Nhập các loại file hình ảnh, cách nhau bằng dấu phẩy (ví dụ: jpg,png hoặc để trống để xử lý tất cả): "
    ).strip()

    # Process input types
    if input_types_raw:
        # Split the input types and convert to list
        input_types = input_types_raw.split(",")
    else:
        # Assign None so all files are handled
        input_types = None

    resize_images(folder_path, input_types)