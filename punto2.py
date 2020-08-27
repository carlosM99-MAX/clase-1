def numero_primo():
    numero = int(input("Escriba un numero= "))
    contador = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        print("Es primo")
        return True
    else:
        print("No es primo")
        return False

def main():
    numero_primo()

if __name__ == "__main__":
    main()