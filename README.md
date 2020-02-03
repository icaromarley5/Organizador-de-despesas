# Organizador-de-despesas

Script que lê um arquivo de extensão csv e cria uma pasta e nela armazena arquivos txt sobre despesas.<br>
Com esse script, é possível separar e identificar os ativos que drenam mais caixa de uma pessoa jurídica ou física.

### Observações
As despesas são armazenadas em arquivos de acordo com sua fonte (passivo), junto com uma soma total ao final de cada arquivo.<br>
O nome da pasta varia de acordo com o ano e mês da execução. <br>
Os arquivos são nomeados de acordo com suas fontes de despesa.

## Tecnologias utilizadas
Feito em Python, utilizando as bibliotecas pandas e tabulate.

## Como utilizar: 
1. crie um arquivo csv com as despesas anotadas sob as colunas DATA, NOME, LOCAL E VALOR<br>
2. Coloque na mesma pasta do arquivo "main.py", sob o nome de "DESPESAS - Página1.csv"<br>
3. Execute o comando no terminal: python main.py<br>
4. Aguarde o fim da execução

