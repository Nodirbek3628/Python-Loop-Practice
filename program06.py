import random            #Cheklangan urinishli o‘yin

num = random.randint(1,10)
# print(num) randint aniqlab bergan maxfiy son 
count = 0

while count < 3:
    option = int(input("soni kiritng: "))
    count += 1
    if option == num:
        print(f"siz to'gri topdingiz.")
        break
    else:
        print(f"siz notug'ri topdingiz:")
else:
    print("Urinishlar tugadi:")
    
