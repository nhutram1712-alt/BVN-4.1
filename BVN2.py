
P = "DangNhuTram"
STT = 49

# Tạo chuỗi kết quả rỗng
chuoi_ma_hoa = ""

# Duyệt từng ký tự trong chuỗi gốc
for ky_tu in P:
    # Kiểm tra nếu là chữ cái
    if ky_tu.isalpha():
        # Nếu là chữ hoa thì dùng 'A', nếu là chữ thường thì dùng 'a'
        if ky_tu.isupper():
            co_so = ord('A')
        else:
            co_so = ord('a')
        
        # Mã hóa ký tự bằng cách cộng STT và lấy dư theo 26
        ma_hoa = (ord(ky_tu) - co_so + STT) % 26
        ky_tu_moi = chr(ma_hoa + co_so)
        
        # Thêm ký tự đã mã hóa vào chuỗi kết quả
        chuoi_ma_hoa += ky_tu_moi
    else:
        # Nếu không phải chữ cái thì giữ nguyên
        chuoi_ma_hoa += ky_tu

# In ra kết quả
print("Chuỗi đã mã hóa:", chuoi_ma_hoa)