pi = 3.14159

def retroceder():
    print("1. Calculate")
    print("2. Go back")
    sub = input("Choose: ")
    return sub

while True:
    print("--- Enter the Figure 2D---")
    print("1. Triangulo")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Triangulo Rectangulo")
    print("------------------------")
    print("--- Enter the Figure 3D---")
    print("5. Cubo")
    print("6. Esfera")
    print("7. Cilindro")
    print("8. Cono")
    print("0. Exit")

    opcion = input("Enter the Figure: ")

    if opcion == "0":
        print("Bye")
        break

    elif opcion == "1":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            base  = float(input("Enter the base: "))
            altura = float(input("Enter the height: "))
            lado  = float(input("Enter side 1: "))
            area      = base * altura / 2
            perimeter = lado * 3
            print("Area:", area)
            print("Perimeter:", perimeter)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "2":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            radio     = float(input("Enter radio: "))
            area      = pi * radio ** 2
            perimeter = 2 * pi * radio
            print("Area:", area)
            print("Perimeter:", perimeter)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "3":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            base   = float(input("Enter base: "))
            altura = float(input("Enter height: "))
            area      = base * altura
            perimeter = 2 * (base + altura)
            print("Area:", area)
            print("Perimeter:", perimeter)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "4":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            cateto1 = float(input("Enter cateto 1: "))
            cateto2 = float(input("Enter cateto 2: "))
            angulo1 = float(input("Enter angulo 1: "))
            angulo2 = float(input("Enter angulo 2: "))
            angulos    = angulo1 + angulo2 + 90
            area       = (cateto1 * cateto2) / 2
            hypotenuse = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
            perimeter  = cateto1 + cateto2 + hypotenuse
            print("Area:", area)
            print("Perimeter:", perimeter)
            print("Hypotenuse:", hypotenuse)
            print("Suma angulos:", angulos)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "5":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            lado    = float(input("Enter lado: "))
            volumen = lado ** 3
            area    = 6 * lado ** 2
            print("Volumen:", volumen)
            print("Area:", area)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "6":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            radio      = float(input("Enter radio: "))
            area       = 4 * pi * radio ** 2
            volumen    = (4/3) * pi * radio ** 3
            print("Area:", area)
            print("Volumen:", volumen)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "7":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            altura  = float(input("Enter altura: "))
            radio   = float(input("Enter radio: "))
            area    = 2 * pi * radio * (radio + altura)
            volumen = pi * radio ** 2 * altura
            print("Area:", area)
            print("Volumen:", volumen)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    elif opcion == "8":
        sub = retroceder()
        if sub == "2":
            continue
        try:
            radio      = float(input("Enter radio: "))
            altura     = float(input("Enter altura: "))
            generatriz = float(input("Enter generatriz: "))
            area       = pi * radio * (radio + generatriz)
            volumen    = (1/3) * pi * radio ** 2 * altura
            print("Area:", area)
            print("Volumen:", volumen)
        except ValueError:
            print("⚠ Please enter valid numbers only!")

    else:
        print("⚠ Invalid option!")