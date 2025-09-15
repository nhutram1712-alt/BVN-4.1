# Hàm mã hóa Caesar
def ma_hoa_caesar(plaintext, k):
    ket_qua = ""  # Chuỗi kết quả sau khi mã hóa

    # Giới hạn số dịch chuyển trong phạm vi 0–25
    so_dich = k % 26

    # Duyệt từng ký tự trong chuỗi gốc
    for ky_tu in plaintext:
        # Nếu là chữ cái
        if ky_tu.isalpha():
            # Kiểm tra chữ hoa hay chữ thường
            if ky_tu.isupper():
                ma_ascii = ord(ky_tu)  # Lấy mã ASCII của ký tự
                ma_moi = (ma_ascii - ord('A') + so_dich) % 26 + ord('A')
                ky_tu_moi = chr(ma_moi)
            else:
                ma_ascii = ord(ky_tu)
                ma_moi = (ma_ascii - ord('a') + so_dich) % 26 + ord('a')
                ky_tu_moi = chr(ma_moi)

            ket_qua += ky_tu_moi  # Thêm ký tự đã mã hóa vào kết quả
        else:
            ket_qua += ky_tu  # Nếu không phải chữ cái thì giữ nguyên

    return ket_qua  # Trả về chuỗi đã mã hóa

# Dữ liệu đầu vào
plaintext = "DangNhuTram"
k = 49

# Gọi hàm để mã hóa
chuoi_ma_hoa = ma_hoa_caesar(plaintext, k)

# In kết quả ra màn hình
print("Chuỗi sau khi mã hóa:", chuoi_ma_hoa)