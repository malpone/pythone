numero = int(input("Inserisci un Numero: "))
lettera = input ("Inserisci una Lettera: ")
z= 0
a=0
for num in range(numero):
    print(" " * (numero-a), lettera * (1 + z))
    z+=2
    a+=1
   