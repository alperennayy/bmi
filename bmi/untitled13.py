
a = float(input("kilonuzu giriniz : ")) #kg cinsinden
b = float(input("boyunuzu giriniz : ")) #metre cinsinden

bmi = a/b**2

if bmi<=18.5 : 
    print("zayıf")
elif  bmi>18.5 and bmi<=24.9 : 
    print("normal")
elif bmi>25 and bmi<=29.9 : 
    print("kilolu")
elif bmi>30 :
    print("obez")
    
    
    



