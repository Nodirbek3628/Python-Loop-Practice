answer = "Toshkent"
                             #Dastur foydalanuvchidan “O‘zbekiston poytaxti nima?” deb so‘raydi. “Toshkent” deb to‘g‘ri javob berguncha so‘rashda davom etadi
count = 0
while count < 3 :
    option = input("O'zbekiston poytaxti nima?")
    count += 1
    if option.capitalize() == answer:
        print(f"siz to'g'ri topdingiz urinishlar soni  {count} ")
        break
else:
    print(f"Notug'ri topdingz urunishlar soni  {count}")