import pandas as pd
import numpy as np
import xlrd
import matplotlib
import os
import math
pi = math.pi
import matplotlib.pyplot as plt

#cambia cartella
percorsoPrincipaleProgramma = "C:/Users/Edoardo/Desktop" #FISSO
percorsoPrincipaleProgramma = "C:/Users/edoar/Desktop" #PORTATILE
os.chdir(percorsoPrincipaleProgramma)

#         INDICE ANALITICO PROGRAMMA:
# 1.  DEFINZIONE FUNZIONI
# 2.  DEFINIZIONE VARIABILI PRINCIPALI
# 3.  INIZIO SCRIPT
# 4.  GRAFICHERIA E PRINTERIA
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
        if (math.isnan(numeroDaTestare)) & (len(vettoreRisultato) == 0):
            vettoreRisultato.append(0)
        elif (math.isnan(numeroDaTestare)):
            vettoreRisultato.append(vettoreRisultato[-1])
        else:
            vettoreRisultato.append(numeroDaTestare)
    return vettoreRisultato

#converti data in formato leggibile dalla libreria pandas
def convertiData2americano(vettoreDate, nomeColonnaDate):
    return pd.to_datetime(vettoreDate[nomeColonnaDate], format="%d/%m/%Y", errors='coerce').tolist()

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
nomePercorsoFileBilancio = str("TREND_SPESE_TOTALI.ods")
dataIngresso = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "A") 
motivoIngresso = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "B")
colonnaEntrate = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "C")
colonnaUscite = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "D")
colonnaTotale = pd.read_excel(nomePercorsoFileBilancio, index_col=None, engine="odf", header= None, sheet_name = "Foglio1", skiprows= 3, usecols = "E")

#elimina le prime 3 colonne del vettore, che hanno solo instestazione, spazio e formattaione

# trasforma tutti i vettori in float per sicurezza (non so in che formato li sta leggendo)
nomeColonnaEntrate = colonnaEntrate.columns[0]
nomeColonnaUscite = colonnaUscite.columns[0]
nomeColonnaTotale = colonnaTotale.columns[0]

colonnaEntrate_float = colonnaEntrate[nomeColonnaEntrate].astype(float).tolist()
colonnaUscite_float = colonnaUscite[nomeColonnaUscite].astype(float).tolist()
colonnaTotale_float = colonnaTotale[nomeColonnaTotale].astype(float).tolist()


# fai sparire tutti in nan e metti un valore costante identico al precedente se li trovi
colonnaEntrateSenzaNan = creaVettoreNumerico(colonnaEntrate_float)
colonnaUsciteSenzaNan = creaVettoreNumerico(colonnaUscite_float)
colonnaTotaleSenzaNan = creaVettoreNumerico(colonnaTotale_float)

#sistema la data, pandas le legge in americano
nomeColonnaDate = dataIngresso.columns[0]
dataIngressoConvertita = convertiData2americano(dataIngresso, nomeColonnaDate)
dataIngressoMaSoloDataOh =  [stocazzo.date() for stocazzo in dataIngressoConvertita]
ristocazzo = pd.to_datetime(dataIngressoMaSoloDataOh)


### 4. GRAFICHERIA E PRINTERIA 
plt.plot(ristocazzo, colonnaTotaleSenzaNan, color='black', linewidth=2, label='TREND TOTALE SPESE')
plt.plot(ristocazzo, colonnaEntrateSenzaNan, color='blue', linewidth=1, label='TREND TOTALE SPESE')
plt.plot(ristocazzo, colonnaUsciteSenzaNan, color='red', linewidth=1, label='TREND TOTALE SPESE')
plt.grid()

# test pulizia date
#plt.plot(ristocazzo)



### 5.  COMANDI LOGICAMENTE IN FONDO AL CODICE

plt.show()

