m1 = []
m2 = []

def matrices():
    t = int(input("Defina matriz: "))
    print("Ingrese valores para la matriz 1: \n")
    valoresMatrices(m1, t)
    print("Ingrese valores para la matriz 2: \n")
    valoresMatrices(m2, t)
    print("MENU\n 1- Suma\n 2- Resta\n 3- Multiplicacion\n 4- Imprimir\n 0- Salir")
    op = int(input("Seleccione una opcion: "))
    while op!=0:
        result = []
        temp = []
        if op==1:
            for i in range(t):
                for j in range(t):
                    temp.append(m1[i][j] + m2[i][j])
                result.append(temp)
                temp = []
            print("El resultado de la suma es: ", result)
        elif op==2:
            for i in range(t):
                for j in range(t):
                    temp.append(m1[i][j] - m2[i][j])
                result.append(temp)
                temp = []
            print("El resultado de la resta es: ", result)
        elif op==3:
            for i in range(t):
                for j in range(t):
                    temp.append(m1[i][j] * m2[i][j])
                result.append(temp)
                temp = []
            print("El resultado es: ", result)
        elif op==4:
            print("La matriz 1 es: ",m1)
            print("La matriz 2 es: ",m2)
        elif op==4:
            break
        else:
            print("Opcion no valida")
        print("MENU\n 1- Suma\n 2- Resta\n 3- Multiplicacion\n 4- Imprimir\n 0- Salir")
        op = int(input("Seleccione una opcion: "))

def valoresMatrices(m, t):
    temp = []
    for i in range(t):
        for j in range(t):
            num = int(input("("+str(i)+","+str(j)+") "))
            temp.append(num)
        m.append(temp)
        temp = []

matrices()