import math

def get_name():
  first_name = input("Please enter your first name:")
  last_name = input("Please enter your last name:")
  print(f"Your name is {first_name} {last_name}")

def get_age():
    age = input("please enter your age:")
    if age.isdigit():
        if age > 0:
            print(f"Vous aurez {int(age) + 100} dans 100 ans")
            return
        else:
            print("Votre age doit être un entier positif")
            return get_age()
    else:
        print("Votre age doit être un entier positif")
        return get_age()

def volume(rayon,hauteur):
    if isinstance(rayon,(int, float)) and isinstance(hauteur, (int, float)):
        print(f"Le volume est {round((math.pi * rayon**2 * hauteur)/3, 2)}")
        return
    else: 
        print(f"Hauteur et rayon doivent être des nombres")

def odd_even():
    a = int(input("Donnez un nombre: "))
    if a.isdigit():
        if a % 2: 
            print(f'{a} est impair')
            return
        else: 
            print(f'{a} est pair')
            return
    else:
        print("Veuillez donner un nombre!")
        odd_even()

def fibonacci():
    result = [0,1]
    print("Entrez un nombre :")
    n = input()
    if n.isdigit():
        n = int(n)
        if n > 0:
            for i in range(2, n + 1):
                next = result[-1] + result[-2]
                result.append(next)
            result = ", ".join([str(i) for i in result])
            print(f"La suite fibonacci est :\n {result}")
        else:
            print("Veuillez entrer un entier positif")
            return fibonacci()
    else:
        print("Veuillez entrer un entier positif")
        return fibonacci()

def intersect(list1,list2):
    if isinstance(list1,list) and isinstance(list2,list):
        return [i for i in list1 if i in list2]
    else:
        print(f'{list1} et {list2} doivent être des listes')
        return

def palyndrom(str):
    invert = "".join([*str][::-1])
    if invert == str: print("Palyndrom")
    else: print("Pas un Palyndrom")

def doublons(list):
    occurences = []
    result = []
    for i in list:
        if i not in occurences: 
            result.append(i)
            occurences.append(i)
    print(result)

def pgcd(num1, num2):
    pgcd = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0: pgcd.append(i)
    return max(pgcd)
def ppcm(num1, num2):
    print(f'ppcm est {int((num1*num2)/pgcd(num1,num2))}')

def pgcd_ppcm(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
         print(f'pgcd est {pgcd(num1,num2)}')
         ppcm(num1, num2)
    else:
        print(f"{num1} et {num2} doivent être des entiers")

def valid_ip(address):
    if isinstance(address,str):
        temp = address.split(".")

        if len(temp) != 4:
            print(f"invalid IP address {address}")
            return

        for element in temp:
            if element.isdigit():
                if int(element) < 0 or int(element) > 255:
                    print(f"invalid IP address {address}")
                    return
            else:
                print(f"invalid IP address {address}")
                return
    
        print(f"valid IP address {address}")
    else:
        print(f"invalid IP address {address}")