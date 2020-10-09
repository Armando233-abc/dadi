import random
import threading

class THREAD:
    thread = []
    punteggio_dadi = ""
    
    def inizia(self, i): # creazione e avviamento thread
        t = threading.Thread(target=self.dadi)
        self.thread.append(t)
        self.thread[i].start()
    
    def aspetta(self, i): # aspetta la fine dei thread
        self.thread[i].join()

    def dadi(self): # mescolamento e scelta del numero
        numeri_dei_dadi = [1, 2, 3, 4, 5, 6]
        
        for i in range(10):
            random.shuffle(numeri_dei_dadi)
        
        for i in range(self.N_dadi):
            if (i < self.N_dadi-1):
                self.punteggio_dadi += str(random.choice(numeri_dei_dadi)) + ","
            else:
                self.punteggio_dadi += str(random.choice(numeri_dei_dadi))


class GIOCATORE(THREAD):

    def __init__(self, nome, N_dadi): # nome e numero dei dadi
        self.nome = nome
        self.N_dadi = N_dadi
    

    def stampa(self): # stampa
        print(f"Al giocatore {self.nome} sono usciti i numeri ({self.punteggio_dadi})")
