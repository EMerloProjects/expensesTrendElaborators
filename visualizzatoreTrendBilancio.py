import pandas as pd
import numpy as np
import xlrd
import matplotlib
import os
import math
pi = math.pi
import matplotlib.pyplot as plt

#cambia cartella
percorsoPrincipaleProgramma = "C:/Users/e.merlo/Desktop/PROGETTI/AAA - ROGNE QUOTIDIANE/CAZZI BILANCI"
os.chdir(percorsoPrincipaleProgramma)

#         INDICE ANALITICO PROGRAMMA:
# 1.  DEFINZIONE FUNZIONI
# 2.  DEFINIZIONE VARIABILI PRINCIPALI
# 3.  INIZIO SCRIPT
# 4.  PRINTERIA
# 4.  COMANDI LOGICAMENTE IN FONDO AL CODICE

### 1. DEFINIZIONE FUNZIONI

# Funzione per pulire il terminale
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# crea vettore normale di numeri ma mette zeri invece di NaN nelle varie posizioni
def creaVettoreNumerico(vettoreDaPulire):
    vettoreRisultato = []
    for i in range(len(vettoreDaPulire)):
        numeroDaTestare = vettoreDaPulire[i]
        if math.isnan(numeroDaTestare):
            vettoreRisultato.append(0)
        else:
            vettoreRisultato.append(numeroDaTestare)
    return vettoreRisultato



### 2. DEFINIZIONE VARIABILI PRINCIPALI

dataIngresso = []
motivoIngresso = []
colonnaEntrate = []
colonnaUscite = []
colonnaTotale = []

percentualeUscitaSuTotale = []
percentualeEntrataSuTotale = []

### 3. INIZIO SCRIPT
clearTerminal()

#leggi file .ods e importa le varie caselle, usa specialmente il motore custom per il formato odf
nomePercorsoFileBilancio = str("S2 - 2023.ods")
dataIngresso = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "A") 
motivoIngresso = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "B")
colonnaEntrate = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "C")
colonnaUscite = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "D")
colonnaTotale = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "E")

#elimina le prime 3 colonne del vettore, che hanno solo instestazione, spazio e formattaione


# print(colonnaEntrate)
# print(colonnaUscite)
# print(colonnaTotale)

# trasforma tutti i vettori in float per sicurezza (non so in che formato li sta leggendo)
colonnaEntrate_float = list(map(float, colonnaEntrate))
colonnaUscite_float = list(map(float, colonnaUscite))
colonnaTotale_float = list(map(float, colonnaTotale))

print('\n')
print(colonnaEntrate_float)



colonnaEntrateSenzaNan = creaVettoreNumerico(colonnaEntrate)
colonnaTotaleSenzaNan = creaVettoreNumerico(colonnaEntrate)
print('\n')
print('\n')
print('\n')
print('PRIMA VERSIONE')
print(colonnaTotale)
print('\n')
print(len(colonnaEntrateSenzaNan))
print(len(colonnaTotaleSenzaNan))

for p in range(len(colonnaEntrateSenzaNan)):
    percentualeEntrataSuTotale.append((colonnaEntrateSenzaNan[p])/(colonnaTotaleSenzaNan[p]))

#print(percentualeEntrataSuTotale)


### 4.  PRINTERIA

plt.plot(dataIngresso, colonnaTotale, color='black', linewidth=2, label='TREND TOTALE SPESE')





### 4.  COMANDI LOGICAMENTE IN FONDO AL CODICE

#plt.show()

