# %%
import pandas as pd
import csv
import chardet
import re
import shutil
import os
import glob
import csv
from thefuzz import process

# %%
MAIN_DF = pd.read_csv("cleanData11-12-01.csv")
df_wydatki = MAIN_DF

### Usuwanie zbędnych kolumn
cols = ["Data księgowania", "Tytuł", "Nr rachunku", "Nazwa banku", "Szczegóły", "Nr transakcji", "Waluta", "Waluta.1", "Kwota płatności w walucie", "Waluta.2", "Konto", "Saldo po transakcji", "Waluta.3"]
colsIndex = []

for title in cols:
    index = df_wydatki.columns.get_loc(title)
    colsIndex.append(index)

df_wydatki.drop(df_wydatki.columns[colsIndex],axis=1,inplace=True)

### Usuwanie ostatnich wierszy
ostatnieWiersze = df_wydatki.tail(3).index
df_wydatki.drop(ostatnieWiersze, inplace = True)
df_wydatki

### Konsolidacja kolumn z wydatkami
df_wydatki['Kwota transakcji (waluta rachunku)'] = df_wydatki[['Kwota transakcji (waluta rachunku)', 'Kwota blokady/zwolnienie blokady']].apply(lambda x: ' '.join(x.dropna()), axis=1)
del df_wydatki["Kwota blokady/zwolnienie blokady"]
df_wydatki["Dane kontrahenta"] = df_wydatki["Dane kontrahenta"].str.upper()

### Sortowanie alfabetyczne kol. Dane kontrahenta
df_wydatki.sort_values("Dane kontrahenta", inplace=True)
df_wydatki = df_wydatki.reset_index(drop=True)

df_wydatki.to_csv("initialData11-12-01.csv", sep=',', encoding='utf-8', index=False, header=True)

df_wydatki


