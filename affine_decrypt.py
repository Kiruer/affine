import math
stupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = 26
def get_key():
    print("Nhap khoa k = (a,b): ")
    a = input("Nhap a: ")
    a = int(a)
    b = input("Nhap b: ")
    b = int(b)
    return a,b
#Decrypt function/ Ham giai ma
def decrypt(cp):
    d_txt = []
    for i in cp.upper():
        if i.isalpha():
            d = (pow(a,-1,26)*(stupper.index(i) - b))%m
            d_txt.append(stupper[d])
        else:
            d_txt.append(i)
    return "".join(d_txt)
print("\t MA AFFINE")
print("1. Giai ma \n2. Tham ma")
ciphertext = str(input("Nhap van ban can giai/tham ma: "))
while True:
    x = input("Chon 1 so de thuc hien nhiem vu: ")
    x = int(x)
    if x == 1:
        a,b = get_key()       
        decipher_text = decrypt(ciphertext)
        print("Ban ro: ",decipher_text)
    elif x == 2:
        def modInverse(a, m): 
            a = a % m; 
            for x in range(1, m) : 
                if ((a*x)%m == 1) : 
                    return x 
            return 1
        #Tham ma
        for b in range(1,26,1):
            for a in range(26):
                if math.gcd(a,26)==1:
                    bf_txt = []
                    a_inv = modInverse(a,26)
                    for i in ciphertext.upper():
                        if i in stupper:
                            yb = stupper.find(i)
                            bf = (a_inv*(yb - b))%m
                            if bf < 0:
                                bf+=26
                            bf_txt.append(stupper[bf])
                        else:
                            bf_txt.append(i)              
                    print("Key(%d,%d): %s" %(a,b,"".join(bf_txt)))
    else:
        print("Ket thuc")
        break