pi = 3.14159
L = True
f = True


def retroceder():
    print("1. Calcular")
    print("2. Volver")
    sub = input("Elige: ")
    return sub


while L:
    print("==============================")
    print(" CALCULADORA GEOMETRICA")
    print("==============================")
    print("--- Figuras 2D ---")
    print("1. Triangulo")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Triangulo Rectangulo")
    print("--- Figuras 3D ---")
    print("5. Cubo")
    print("6. Esfera")
    print("7. Cilindro")
    print("8. Cono")
    print("0. Salir")
    print("==============================")

    opcion = input("Ingresa la figura: ")

    if opcion == "0":
        print("¡Hasta luego!")

        f = False

    # ─── TRIANGULO
    elif opcion == "1":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Triangulo ---")
        print("1. Area")
        print("2. Perimetro")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                base = float(input("Ingresa la base: "))
                altura = float(input("Ingresa la altura: "))
                area = base * altura / 2

                print(" Area:", area)

            elif sub2 == "2":
                lado = float(input("Ingresa el lado: "))
                perimetro = lado * 3

                print(" Perimetro:", perimetro)

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── CIRCULO
    elif opcion == "2":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Circulo ---")
        print("1. Area")
        print("2. Perimetro")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                radio = float(input("Ingresa el radio: "))
                if radio > 0:
                    area = pi * radio**2

                    print(" Area:", area)

                else:
                    print(" El radio debe ser mayor que 0!")

            elif sub2 == "2":
                radio = float(input("Ingresa el radio: "))
                if radio > 0:
                    perimetro = 2 * pi * radio

                    print(" Perimetro:", perimetro)

                else:
                    print(" El radio debe ser mayor que 0!")

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── RECTANGULO
    elif opcion == "3":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Rectangulo ---")
        print("1. Area")
        print("2. Perimetro")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                base = float(input("Ingresa la base: "))
                altura = float(input("Ingresa la altura: "))
                area = base * altura

                print(" Area:", area)

            elif sub2 == "2":
                base = float(input("Ingresa la base: "))
                altura = float(input("Ingresa la altura: "))
                perimetro = 2 * (base + altura)

                print(" Perimetro:", perimetro)

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── TRIANGULO RECTANGULO
    elif opcion == "4":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Triangulo Rectangulo ---")
        print("1. Area")
        print("2. Perimetro")
        print("3. Hipotenusa")
        print("4. Angulo 2")
        print("5. Cateto faltante")
        print("6. sen opuesto")
        print("7. cos adyacente")
        print("8. tan opuesto")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                cateto1 = float(input("Ingresa cateto 1: "))
                cateto2 = float(input("Ingresa cateto 2: "))
                area = (cateto1 * cateto2) / 2

                print(" Area:", area)

            elif sub2 == "2":
                cateto1 = float(input("Ingresa cateto 1: "))
                cateto2 = float(input("Ingresa cateto 2: "))
                hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
                perimetro = cateto1 + cateto2 + hipotenusa

                print(" Perimetro:", perimetro)

            elif sub2 == "3":
                cateto1 = float(input("Ingresa cateto 1: "))
                cateto2 = float(input("Ingresa cateto 2: "))
                hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

                print(" Hipotenusa:", hipotenusa)

            elif sub2 == "4":
                angulo1 = float(input("Ingresa angulo 1: "))
                angulo2 = 90 - angulo1

                print(" Angulo 2:", angulo2)

            elif sub2 == "5":
                hipotenusa = float(input("Ingresa la hipotenusa: "))
                cateto1 = float(input("Ingresa cateto 1: "))
                cateto2 = (hipotenusa**2 - cateto1**2) ** 0.5

                print(" Cateto faltante:", cateto2)

            elif sub2 == "6":
                angulo1 = float(input("Ingresa angulo 1 (grados): "))
                hipotenusa = float(input("Ingresa la hipotenusa: "))
                angulo_rad = angulo1 * (pi / 180)
                sen_val = angulo_rad - angulo_rad**3 / 6 + angulo_rad**5 / 120
                opuesto = sen_val * hipotenusa

                print(" Lado opuesto:", opuesto)

            elif sub2 == "7":
                angulo1 = float(input("Ingresa angulo 1 (grados): "))
                hipotenusa = float(input("Ingresa la hipotenusa: "))
                angulo_rad = angulo1 * (pi / 180)
                cos_val = 1 - angulo_rad**2 / 2 + angulo_rad**4 / 24
                adyacente = cos_val * hipotenusa

                print(" Lado adyacente:", adyacente)

            elif sub2 == "8":
                angulo1 = float(input("Ingresa angulo 1 (grados): "))
                cateto1 = float(input("Ingresa cateto adyacente: "))
                angulo_rad = angulo1 * (pi / 180)
                tan_val = angulo_rad - angulo_rad**3 / 3 + angulo_rad**5 / 5
                opuesto = cateto1 * tan_val

                print(" Lado opuesto:", opuesto)

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── CUBO
    elif opcion == "5":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cubo ---")
        print("1. Volumen")
        print("2. Area")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                lado = float(input("Ingresa el lado: "))
                volumen = lado**3

                print(" Volumen:", volumen)

            elif sub2 == "2":
                lado = float(input("Ingresa el lado: "))
                area = 6 * lado**2

                print(" Area:", area)

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── ESFERA
    elif opcion == "6":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Esfera ---")
        print("1. Volumen")
        print("2. Area")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                radio = float(input("Ingresa el radio: "))
                if radio > 0:
                    volumen = (4 / 3) * pi * radio**3

                    print(" Volumen:", volumen)

                else:
                    print("⚠ El radio debe ser mayor que 0!")

            elif sub2 == "2":
                radio = float(input("Ingresa el radio: "))
                if radio > 0:
                    area = 4 * pi * radio**2

                    print(" Area:", area)

                else:
                    print(" El radio debe ser mayor que 0!")

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── CILINDRO
    elif opcion == "7":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cilindro ---")
        print("1. Volumen")
        print("2. Area")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                radio = float(input("Ingresa el radio: "))
                altura = float(input("Ingresa la altura: "))
                if radio > 0:
                    volumen = pi * radio**2 * altura

                    print(" Volumen:", volumen)

                else:
                    print("⚠ El radio debe ser mayor que 0!")

            elif sub2 == "2":
                radio = float(input("Ingresa el radio: "))
                altura = float(input("Ingresa la altura: "))
                if radio > 0:
                    area = 2 * pi * radio * (radio + altura)

                    print(" Area:", area)

                else:
                    print(" El radio debe ser mayor que 0!")

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    # ─── CONO
    elif opcion == "8":
        sub = retroceder()
        if sub == "2":
            continue
        print("--- Cono ---")
        print("1. Volumen")
        print("2. Area")
        sub2 = input("Elige: ")
        try:
            if sub2 == "1":
                radio = float(input("Ingresa el radio: "))
                altura = float(input("Ingresa la altura: "))
                if radio > 0:
                    volumen = (1 / 3) * pi * radio**2 * altura

                    print(" Volumen:", volumen)

                else:
                    print("⚠ El radio debe ser mayor que 0!")

            elif sub2 == "2":
                radio = float(input("Ingresa el radio: "))
                generatriz = float(input("Ingresa la generatriz: "))
                if radio > 0:
                    area = pi * radio * (radio + generatriz)

                    print(" Area:", area)

                else:
                    print("⚠ El radio debe ser mayor que 0!")

            else:
                print(" Opcion invalida!")
        except ValueError:
            print(" Por favor ingresa solo numeros!")

    else:
        print(" Opcion invalida!")
