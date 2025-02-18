# Python Resize Images
Xin chào, mình là Vinh đây. 

[![Python Optimize Images](http://img.youtube.com/vi/aRmBLWA_czA/0.jpg)](http://www.youtube.com/watch?v=aRmBLWA_czA)

Đây là code Python thay đổi kích thước hình ảnh hàng loạt một cách miễn phí, nhanh chóng. Có thể xử lý bao nhiêu cũng được, tốc độ nhanh.

## Giới thiệu
Script này cho phép người dùng thay đổi kích thước các ảnh trong một thư mục được chỉ định thành hai kích thước khác nhau (nhỏ và trung bình) trong khi vẫn giữ nguyên tỷ lệ khung hình. Các ảnh đã được thay đổi kích thước sẽ được lưu trong cùng thư mục với hậu tố `-small` và `-medium` trong tên tệp.

## Function
**`resize_images(folder_path, input_types=None, small_width=320, medium_width=640)`**: Hàm chính để thay đổi kích thước hình ảnh.

Kích Thước Mặc Định
- **Chiều Rộng Kích Thước Nhỏ:** 320 pixel
- **Chiều Rộng Kích Thước Trung Bình:** 640 pixel

**Tham số:**
  - `folder_path`: Đường dẫn đến thư mục chứa ảnh.
  - `input_types`: Danh sách tùy chọn các phần mở rộng tệp cần xử lý.
  - `small_width`: Chiều rộng của ảnh kích thước nhỏ (mặc định: 320 pixel).
  - `medium_width`: Chiều rộng của ảnh kích thước trung bình (mặc định: 640 pixel).
- Lưu các ảnh đã thay đổi kích thước trong cùng thư mục với tên tệp đã được cập nhật.

## Output
Mỗi hình ảnh sau khi thay đổi kích thước sẽ được lưu trong cùng thư mục với:
  - Hậu tố `-small` cho ảnh kích thước nhỏ.
  - Hậu tố `-medium` cho ảnh kích thước trung bình.

### **Ví Dụ Đầu Ra**

Với một hình ảnh `example.jpg` trong thư mục:
- Ảnh kích thước nhỏ: `example-small.jpg`
- Ảnh kích thước trung bình: `example-medium.jpg`

### **Lưu Ý:**

- Đảm bảo đường dẫn thư mục tồn tại và chứa các tệp ảnh hợp lệ.
- Việc xử lý các tệp không phải ảnh hoặc định dạng không được hỗ trợ sẽ dẫn đến lỗi.

----
Đọc thêm tại: https://vinhweb.com/blog/code-python-optimize-toi-uu-hinh-anh-mien-phi

Nhiều source code hay hơn nữa tại website: https://vinhweb.com/.

Hãy mua để ủng hộ Vinh phát triển thêm nhé, cảm ơn bạn.

## Hướng dẫn setup:
Hướng setup Python Project để chạy được source này tại [đây](https://mango-freesia-da4.notion.site/Doc-H-ng-d-n-Setup-Python-Project-VinhWeb-19274673f5db80679725d682c13c7f90?pvs=74)
