#Delta Kullanarak Kök Bulma


print("Programa Hoşgeldiniz. ax^2+bx+c formatına göre istenen değerleri giriniz.")

a= int(input("a değerini giriniz."))
b= int(input("b değerini giriniz."))
c= int(input("c değerini bulunuz."))



print ("Oluşan denklem: {}x^2+{}x+{}".format(a,b,c))

delta= b**2 - (4*a*c)

x1= (-b+(delta**0.5)) / (2*a)
x2= (-b-(delta**0.5)) / (2*a)

print("Birinci kök:{}\nİkinci kök:{}".format(x1,x2))