# Generare il nome di una band dal nome della città d'origine e di un animale domestico

print("\n**** GENERA IL NOME DELLA TUA BAND ****") #Stampa a schermo il titolo del programma

citta=input("\nInserisci le iniziali della città in cui sei nato? ") #La Variabile "citta" dell'Oggetto di tipo stringa avrà un valore definito dall'utente
animale=input("\nInserisci il nome tuo animale domestico (ipotetico)? ") #La Variabile "animale" dell'Oggetto di tipo stringa avrà un valore definito dall'utente

band=citta + animale #La Variabile "band" dell'Oggetto di tipo string sarà l'unione dei valori delle due stringhe precedenti, insertie dall'utente.

print("\n\nIl nome della tua band sarà " + band.upper() + " !") #Stampa a schermo questa stringa e rendi la stringa "band" maiuscola.

risposta=input("\n\nTi piace? (Si/No) ") #Chiedi risposta (stringa) all'utente

if risposta=="Si": #Inizio Ciclo IF-ELSE per l'analisi della condizione "risposta" in merito al valore stringa SI/NO, definito dall'utente.
    print("\nOttimo! Grazie per aver usato questo programma! :) \n\n")
else:
    print("\nMi dispiace, ma dovrai fartene una ragione! :)\n\n")
