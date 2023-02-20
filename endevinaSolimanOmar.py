# Omar Soliman Gil

from random import randint


# Acumuladors
intents = 1
numax = 101
numin = 0
partidanova = True
partides = 1
premi = 0
minintent = 999
maxintent = 0
medintent = 0


# Bucle per a jugar
while partidanova:

    # Cambiem el numero aleatori i demanem quants intents podem fer

    aleatorio = int(randint(1,100))
    trais = int(input("Quants intents es poden fer? "))

    # Fem un bucle per a endevinar
    for i in range(1, trais+1):
        
        num = int(input("Adivina el numero: "))

        # Si el numero no es el indicat, es cambien els marges
        if num < aleatorio:
            if num > numin and num < aleatorio:
                numin = num
            print(f"No. És major. Està entre {numin+1} i {numax-1}")
            intents += 1    

        elif num > aleatorio:
            if num < numax and num > aleatorio:
                numax = num
            print(f"No. És menor. Està entre {numin+1} i {numax-1}")
            intents += 1

        # Si encerta el numero, s'acaba la partida
        elif num == aleatorio:
            print(f"Molt bé! Ho has encertat en {intents} intents.")
            premi += 1
            medintent += intents
            break
    
    # Si s'acaben els intents, s'acaba la partida
    else:
        print(f"Has superat els intents i no ho has endevinat. El numero era {aleatorio}.")
        intents = 0
        break

    # Fem que si es fica un numero fora del rang no cambie el max i min   
    if intents < minintent:
        minintent = intents
        
    elif intents > maxintent:
        maxintent = intents

    # Al acabar la partida preguntem si volem jugar altra i fem les funcions pertinents
    continua = input("Vols jugar altra partida?(s/n) ")
    if continua == "s" or continua == "S":
        numax = 101
        numin = 0
        partides += 1
        intents = 0
        
        continue
    
    elif continua == "n" or continua == "N":
        partidanova = False
        print(f"Has jugat {partides} partides.")
        print()
        print("PREMI \n"*premi )
        print(f"La mitja d'intents de les partides guanyades es {medintent/premi}")
        print(f"La partida guanyada en menos intents ha sigut en {minintent} intents.\nLa partida guanyada en mes intents ha sigut en {maxintent} intents.")
        
    