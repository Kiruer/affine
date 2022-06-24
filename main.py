import math
stupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = 26
#Initiate the key for encoding/ Khởi tạo khóa cho việc mã hóa
def get_key():
    print("Nhap khoa k = (a,b): ")
    a = input("Nhap a: ")
    a = int(a)
    if math.gcd(a,m)!=1:
        raise ValueError("a, m phai nguyen to cung nhau")
    else:
        b = input("Nhap b: ")
        b = int(b)
    return a,b 
#Encrypt function/ Hàm mã hóa
def encrypt(a,b,pt):
    e_txt = []
    for i in pt.upper():
        if i.isalpha():
#Calculate key function/
#Tìm STT trên dãy ứng vs mỗi kí tự trong stupper rồi trả về giá trị số 
            e = (a*(stupper.index(i))+b)%m
            e_txt.append(stupper[e])
        else:
            e_txt.append(i)
    return "".join(e_txt)
print("\t MA AFFINE")
print("Ma hoa")
a,b = get_key()
ptext = str(input("Nhap van ban can ma hoa:"))
ciphertext = encrypt(a,b,ptext)
print("Ban ma:",ciphertext)
    