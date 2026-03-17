pi = 3.14159


def retroceder():
    print("1. Calculate")
    print("2. Go back")
    sub = input("Choose: ")
    return sub


# Función reutilizable para mostrar resultados con formato uniforme.
# Recibe dos parámetros:
# - label: el nombre del resultado (ejemplo: "Area:", "Volumen:")
# - value: el valor calculado (ejemplo: 6.0, 78.5)
# En vez de repetir los 3 print en cada figura, se llama una sola vez.
def mostrar_resultado(label, value):
    print("------------------------------")
    print("", label, value)
    print("------------------------------")


while True:
    print("==============================")
    print("   GEOMETRIC CALCULATOR")
    print("==============================")
    print("--- 2D Figures ---")
    print("1. Triangle")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Right Triangle")
    print("--- 3D Figures ---")
    print("5. Cube")
    print("6. Sphere")
    print("7. Cylinder")
    print("8. Cone")
    print("0. Exit")
    print("==============================")

    opcion = input("Enter the Figure: ")

    if opcion == "0":
        print("Bye!")
        break

    elif opcion == "1":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Triangle ---")
        print("1. Area")
        print("2. Perimeter")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                base = float(input("Enter base: "))
                altura = float(input("Enter height: "))
                area = base * altura / 2
                mostrar_resultado("Area:", area)

            elif sub2 == "2":
                lado = float(input("Enter side: "))
                perimeter = lado * 3
                mostrar_resultado("Perimeter:", perimeter)

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    elif opcion == "2":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Circle ---")
        print("1. Area")
        print("2. Perimeter")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                radio = float(input("Enter radius: "))
                if radio > 0:
                    area = pi * radio**2
                    mostrar_resultado("Area:", area)
                else:
                    print(" Radius must be greater than 0!")

            elif sub2 == "2":
                radio = float(input("Enter radius: "))
                if radio > 0:
                    perimeter = 2 * pi * radio
                    mostrar_resultado("Perimeter:", perimeter)
                else:
                    print(" Radius must be greater than 0!")

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    elif opcion == "3":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Rectangle ---")
        print("1. Area")
        print("2. Perimeter")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                base = float(input("Enter base: "))
                altura = float(input("Enter height: "))
                area = base * altura
                mostrar_resultado("Area:", area)

            elif sub2 == "2":
                base = float(input("Enter base: "))
                altura = float(input("Enter height: "))
                perimeter = 2 * (base + altura)
                mostrar_resultado("Perimeter:", perimeter)

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    elif opcion == "4":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Right Triangle ---")
        print("1. Area")
        print("2. Perimeter")
        print("3. Hypotenuse")
        print("4. Angle 2")
        print("5. Missing cateto")
        print("6. sin opposite")
        print("7. cos adjacent")
        print("8. tan opposite")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                cateto1 = float(input("Enter cateto 1: "))
                cateto2 = float(input("Enter cateto 2: "))
                area = (cateto1 * cateto2) / 2
                mostrar_resultado("Area:", area)

            elif sub2 == "2":
                cateto1 = float(input("Enter cateto 1: "))
                cateto2 = float(input("Enter cateto 2: "))
                hypotenuse = (cateto1**2 + cateto2**2) ** 0.5
                perimeter = cateto1 + cateto2 + hypotenuse
                mostrar_resultado("Perimeter:", perimeter)

            elif sub2 == "3":
                cateto1 = float(input("Enter cateto 1: "))
                cateto2 = float(input("Enter cateto 2: "))
                hypotenuse = (cateto1**2 + cateto2**2) ** 0.5
                mostrar_resultado("Hypotenuse:", hypotenuse)

            elif sub2 == "4":
                angulo1 = float(input("Enter angle 1: "))
                angulo2 = 90 - angulo1
                mostrar_resultado("Angle 2:", angulo2)

            elif sub2 == "5":
                hypotenuse = float(input("Enter hypotenuse: "))
                cateto1 = float(input("Enter cateto 1: "))
                cateto2 = (hypotenuse**2 - cateto1**2) ** 0.5
                mostrar_resultado("Missing cateto:", cateto2)

            elif sub2 == "6":
                angulo1 = float(input("Enter angle 1 (degrees): "))
                hypotenuse = float(input("Enter hypotenuse: "))
                angulo_rad = angulo1 * (pi / 180)
                sin_val = angulo_rad - angulo_rad**3 / 6 + angulo_rad**5 / 120
                opposite = sin_val * hypotenuse
                mostrar_resultado("Opposite side:", opposite)

            elif sub2 == "7":
                angulo1 = float(input("Enter angle 1 (degrees): "))
                hypotenuse = float(input("Enter hypotenuse: "))
                angulo_rad = angulo1 * (pi / 180)
                cos_val = 1 - angulo_rad**2 / 2 + angulo_rad**4 / 24
                adjacent = cos_val * hypotenuse
                mostrar_resultado("Adjacent side:", adjacent)

            elif sub2 == "8":
                angulo1 = float(input("Enter angle 1 (degrees): "))
                cateto1 = float(input("Enter adjacent cateto: "))
                angulo_rad = angulo1 * (pi / 180)
                tan_val = angulo_rad - angulo_rad**3 / 3 + angulo_rad**5 / 5
                opposite = cateto1 * tan_val
                mostrar_resultado("Opposite side:", opposite)

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    elif opcion == "5":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cube ---")
        print("1. Volume")
        print("2. Area")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                lado = float(input("Enter side: "))
                volumen = lado**3
                mostrar_resultado("Volume:", volumen)

            elif sub2 == "2":
                lado = float(input("Enter side: "))
                area = 6 * lado**2
                mostrar_resultado("Area:", area)

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    elif opcion == "6":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Sphere ---")
        print("1. Volume")
        print("2. Area")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                radio = float(input("Enter radius: "))
                if radio > 0:
                    volumen = (4 / 3) * pi * radio**3
                    mostrar_resultado("Volume:", volumen)
                else:
                    print(" Radius must be greater than 0!")

            elif sub2 == "2":
                radio = float(input("Enter radius: "))
                if radio > 0:
                    area = 4 * pi * radio**2
                    mostrar_resultado("Area:", area)
                else:
                    print(" Radius must be greater than 0!")

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    # CYLINDER
    elif opcion == "7":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cylinder ---")
        print("1. Volume")
        print("2. Area")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                radio = float(input("Enter radius: "))
                altura = float(input("Enter height: "))
                if radio > 0:
                    volumen = pi * radio**2 * altura
                    mostrar_resultado("Volume:", volumen)
                else:
                    print("⚠ Radius must be greater than 0!")

            elif sub2 == "2":
                radio = float(input("Enter radius: "))
                altura = float(input("Enter height: "))
                if radio > 0:
                    area = 2 * pi * radio * (radio + altura)
                    mostrar_resultado("Area:", area)
                else:
                    print(" Radius must be greater than 0!")

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    # CONE
    elif opcion == "8":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cone ---")
        print("1. Volume")
        print("2. Area")
        sub2 = input("Choose: ")
        try:
            if sub2 == "1":
                radio = float(input("Enter radius: "))
                altura = float(input("Enter height: "))
                if radio > 0:
                    volumen = (1 / 3) * pi * radio**2 * altura
                    mostrar_resultado("Volume:", volumen)
                else:
                    print(" Radius must be greater than 0!")

            elif sub2 == "2":
                radio = float(input("Enter radius: "))
                generatriz = float(input("Enter slant height: "))
                if radio > 0:
                    area = pi * radio * (radio + generatriz)
                    mostrar_resultado("Area:", area)
                else:
                    print(" Radius must be greater than 0!")

            else:
                print(" Invalid option!")
        except ValueError:
            print(" Please enter valid numbers only!")

    else:
        print(" Invalid option!")
