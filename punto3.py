def numeroperfecto():
    numero = int(input("Escriba un numero= "))
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == numero:
        print("es prefecto")
    else:
        print("no es prefecto")

    return 0


def main():
    numeroperfecto()

if __name__ == "__main__":
    main()