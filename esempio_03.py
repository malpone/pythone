# CONTATORE PUNTI TENNIS
# tiene conteggio dei punti (senza tie break)
# e restituisce vittoria !

punteggio1 = 0
punteggio2 = 0
partita_in_atto = True

while partita_in_atto :
    punto = int(input("Inserire chi ha segnato il punto (1 per giocatore Uno oppure 2 per giocatore Due) : "))
    if punto not in [1, 2] :
        print("ERRORE -Il punto inserito non è valido")
        continue
    
    if punto == 1 :
        punteggio1 += 1
    else : punteggio2 += 1
    
    if (punteggio1 >= 4 and punteggio1 >= punteggio2 + 2) or (punteggio2 >= 4 and punteggio2 >= punteggio1 + 2):
        partita_in_atto = False
        
print ("\n***PARTITA FINITA!***")
 
if punteggio1 > punteggio2 :
    print ("*Vittoria del giocatore Uno*")
else :
    print ("*Vittoria del giocatore Due*")

    