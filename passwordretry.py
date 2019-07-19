password = "a123456"
i = 3
while i != 0 :
    psd = input("請輸入密碼:")
    if psd == password:
        print("登入成功!")
        break
    else :
        i -= 1
        if i == 0 :
            break
        print("密碼錯誤! 還有%d次機會"%i)
if i == 0 :
    print("結束程式!")