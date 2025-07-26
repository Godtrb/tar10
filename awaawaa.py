def invertString(n,long):
    if long == 0:
        return 1
    else:
        print(f"{n[long-1]}", end="")
        return invertString(long-1)
def SumNAt(n):
    if n == 0:
        return 1
    else:
        if (n==1):
            print(f"{n}:", end="")
        else:
            print(f"{n}+", end="")
        return n + SumNAt(n-1)
def RegCount(n):
    if n==0:
        return 1
    else:
        print(f"{n}")
        return RegCount(n-1)
def DecSum(x,lenght):
    if lenght==0:
        return 1
    else:
        return x[lenght-1] + DecSum(x, lenght-1)
def DigCont(x,cont=1):
    if x <= 10**cont:
        return 1
    else:
        return cont,DigCont(x,cont+1)
opt=0

while(opt!=6):
    print("----------Recusrsiv---------------")
    print("1. Inv String")
    print("2. Suma Nat Nums")
    print("3. Reg Count")
    print("4. Suma de Digitos")
    print("5. Cont Dig")
    print("6. Sair")
    opt=int(input(""))
    match (opt):
        case 1:
            dat=input("Ingresa un texto: ")
            largo=len(dat)
            print(invertString(dat,largo))
        case 2:
            num = int(input("Ingresa un numero: "))
            if (num <= 0):
                print("Numero no puede ser 0 o negativo")
            else:
                print(SumNAt(num))
        case 3:
            num = int(input("Ingresa un numero: "))
            if (num <= 0):
                print("Numero no puede ser 0 o negativo")
            else:
                print(RegCount(num))
        case 4:
            num = int(input("Ingresa un numero: "))
            if (num <= 0):
                print("Numero no puede ser 0 o negativo")
            else:
                lengt=len(num)
                print(DecSum(num,lengt))
        case 5:
            num1=int(input("Ingresa un numero: "))
            if (num1 > 0):
                print(DigCont(num1))
            elif (num1 <= 0):
                print("Numero no puede ser negativo o 0")