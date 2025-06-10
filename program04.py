import random                      # Maxfiy kodni topish uyini

secret_code = random.randint(100,999)          

# print(secret_code) bu kodni quysak secret kodimizga randint tanlagan 3 maxfiy parolini bilsak bo'ladi 

while True:
    pasword = int(input("Maxfiy kodni kiriting (3 xonali kodni kiriting) :"))
    if pasword == secret_code:
        print("Siz to'ri topdingiz:")
        break
    else:
        print("Notug'ri urinish yana urinitb ko'ring:")






