def numero_par_o_impar():
    numero = int(input("Escriba un numero= "))
    if numero%2==0:
            print("numero par")
    else:
         print("numero impar")

    return numero

def main(): 
    numero_par_o_impar()

if __name__ == "__main__":
    main()
