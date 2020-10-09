from funzioni import GIOCATORE
import time


N_giocatori = int(input("inserisci il numero di giocatori: "))
N_dadi = int(input("inserisci il numero di dadi da lanciare: "))

player = []

for i in range(N_giocatori): # creazione dell'oggetto giocatore
    nome = str(input(f"Inserisci il nome del giocatore numero {i+1}: "))
    player.append(GIOCATORE(nome, N_dadi))

start = time.time()

for i in range(N_giocatori): #inizio dei thread
    player[i].inizia(i)
    player[i].aspetta(i)

for i in range(N_giocatori): #stampa dei risultati
    player[i].stampa()

end = time.time()

print("tempo: ", end - start)