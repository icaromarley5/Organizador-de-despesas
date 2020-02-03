# Organizador-de-despesas

Script que lê um arquivo de extensão "csv", cria uma pasta e nela armazena arquivos de extensão "txt" sobre despesas.  
Com esse script, é possível separar e identificar os ativos que drenam mais caixa de uma pessoa jurídica ou física.

### Observações
A lista de despesas e uma soma total são armazenadas de forma tabular em arquivos de acordo com a fonte de cada despesa.  
O nome da pasta varia de acordo com o ano e mês da execução (ex: "01_2020").  
Os arquivos são nomeados de acordo com suas fontes de despesa (ex: "CASA.txt").  

## Tecnologias utilizadas
Feito em Python, utilizando as bibliotecas pandas e tabulate.  

## Como utilizar: 
1. Crie um arquivo csv com as despesas anotadas sob as colunas DATA, NOME, LOCAL E VALOR  
2. Coloque na mesma pasta do arquivo "main.py", sob o nome de "DESPESAS - Página1.csv"  
3. Execute o comando no terminal: python main.py  
4. Aguarde o fim da execução  
