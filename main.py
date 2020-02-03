"""
Script para gerar relações de despesas por fonte/imóvel
Cria uma pasta para o mês/ano 
Salva despesas por fonte em arquivos separados
"""

import pandas as pd
from datetime import datetime
import os
from tabulate import tabulate

filePath = 'DESPESAS - Página1.csv'
today = datetime.now()
month = today.month
year = today.year

df = pd.read_csv(filePath,parse_dates=[0],dayfirst=True)

df['VALOR'] = df['VALOR'].str.replace(
    ',', '.').astype(float)

df = df[(df['DATA'].dt.month == month) & (df['DATA'].dt.year == year)]

if not df.empty:
    dirName = f'DESPESAS {month:02d} {year}'
    if dirName not in os.listdir():
        os.mkdir(dirName)
    for local,group in df.groupby('LOCAL'):    
        group = group.copy()
        total = group['VALOR'].sum()
        total = 'R$ ' + f'{total:.2f}'.replace('.',',')
        group['VALOR'] = group['VALOR'].apply(
            lambda x: f'R$ {x:.2f}'.replace('.',','))
        group['DAY'] = group['DATA'].dt.day.apply(lambda x: f'{x:02d}')
        group = group[['DAY','NOME','VALOR']]
        group.set_index('DAY', inplace=True)
        
        with open(
                dirName + f'/{local}.txt',
                "w") as f:
            f.write(
                f'{local}: DESPESAS EM {month:02d}/{year}' + '\n')
            f.write(tabulate(group).replace('-',''))
            f.write(f'\nTotal: {total}') 