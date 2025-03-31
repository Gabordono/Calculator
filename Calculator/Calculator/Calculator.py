
from random import choice


def add(x, y):
   return  x + y
  
def subtract(x, y):
   return x - y
  

def multiply(x, y):
   return x * y
 

def divide(x, y):
  return x / y
 

def exp(x, y):
   return x ** y
  
def root(x,y):
  return x**(1/y)
 
while True:
    print("\nVálaszd ki a műveletet:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Szorzás")
    print("4. Osztás")
    print("5. Hatványozás")
    print("6. Gyökvonás")
    print("7. Kilépés")

    choice= input("add meg a választásod (1-7): ")

    if choice=="7":
        print("Kilépés")
        break
    elif choice in["1","2","3","4","5","6"]:
        try:
           x = float(input("Add meg az x-et: "))
           y = float(input("Add meg az y-et: "))
        except ValueError:
           print("Hibás bemenet! Számokat adj meg!")
           continue
    if choice == "1":
            print("Eredmény:", add(x, y))
    elif choice == "2":
            print("Eredmény:", subtract(x, y))
    elif choice == "3":
            print("Eredmény:", multiply(x, y))
    elif choice == "4":
            if y == 0:
                print("Hiba: nullával nem osztunk!")
            else:
                print("Eredmény:", divide(x, y))
    elif choice == "5":
            print("Eredmény:", exp(x, y))
    elif choice == "6":
            if y == 0:
                print("Hiba: 0-edik gyök nem értelmezhető!")
            else:
                print("Eredmény:", root(x, y))
    else:
        print("Érvénytelen választás, kérlek 1-7 közötti számot adj meg!")