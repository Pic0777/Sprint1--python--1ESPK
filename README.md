<h1> SIMULADOR DE APOSTAS - FORMULA E </h1>

## Colaboradores
- Iago Kutelak - RM: 554698
- João Vicente - RM: 556561
- Lucca Saraiva Borges - RM: 554608
- Pietro Vitor Pezzente - RM: 557283

# Jogo de Apostas de Corrida

Este é um jogo de apostas de corrida de carros, onde você pode apostar em um dos três pilotos. Dependendo das condições climáticas, os multiplicadores de vitória podem variar, influenciando o resultado das suas apostas.

## Requisitos

- Python 3.x

## Funcionalidades

- Escolha entre três pilotos diferentes.
- Condições climáticas aleatórias que afetam os resultados da corrida.
- Multiplicadores de vitória variáveis com base nas condições climáticas.
- Simulação de voltas e cálculo de tempos para determinar o vencedor.

## Como Jogar

1. **Configuração Inicial**:
   - Certifique-se de ter o Python instalado em seu sistema.

2. **Clone ou Baixe o Código**:
   - Clone o repositório do código-fonte do jogo de apostas de corrida de Fórmula E para o seu computador ou faça o download como um arquivo ZIP e extraia-o para uma pasta local.

3. **Abrindo o Projeto no VSCode**:
   - Abra o Visual Studio Code (VSCode).
   - Vá em `Arquivo` > `Abrir Pasta...` e selecione o diretório onde o código do jogo foi clonado ou extraído.

4. **Configuração do Ambiente de Desenvolvimento**:
   - No VSCode, instale a extensão do Python, se ainda não tiver instalado. Vá para a aba de extensões (ícone de quadrado com quatro pequenos quadrados dentro, na barra lateral esquerda) e procure por "Python". Instale a extensão da Microsoft.
   - Certifique-se de que o VSCode está utilizando a versão correta do Python. Para isso, clique no ícone de seleção do interpretador Python no canto inferior esquerdo do VSCode e selecione a versão correta do Python instalada no seu sistema.

5. **Execução do Código**:
   - Abra o arquivo `formula_e_apostas.py` no VSCode.
   - Para executar o código, você pode utilizar o terminal integrado do VSCode. Vá em `Terminal` > `Novo Terminal` para abrir um novo terminal integrado.
   - No terminal, certifique-se de estar no diretório correto (o mesmo onde o arquivo `simulador_apostas.py` está localizado). Se necessário, use o comando `cd <caminho_para_o_diretório>`.
   - Execute o código digitando `python simulador_apostas.py` no terminal integrado e pressionando Enter.

6. **Siga as Instruções do Jogo**:
   - Ao iniciar o jogo, você será recebido com uma mensagem de boas-vindas e as condições climáticas atuais da corrida serão exibidas.
   - Com base nas condições climáticas, o jogo identificará quais equipes foram favorecidas e quais foram desfavorecidas, junto com os multiplicadores de vitória para cada piloto.
   - Você será solicitado a fazer uma aposta em um dos pilotos disponíveis e a especificar o valor da aposta.
   - O jogo simulará as voltas da corrida e determinará o vencedor com base na menor média de tempo por volta.
   - Dependendo do resultado e das condições climáticas, seu prêmio será calculado e exibido.

7. **Encerramento**:
   - Para encerrar o jogo, basta fechar a janela do terminal ou pressionar `Ctrl + C`.

8. **Aproveite o Jogo**:
   - Divirta-se apostando nas corridas de Fórmula E e veja se você consegue prever o vencedor em diferentes condições climáticas!

Certifique-se de ler as instruções e mensagens exibidas durante o jogo para entender completamente como jogar e desfrutar da experiência. Boa sorte e divirta-se!


## Estrutura do Código

```python
import random

# Definição das equipes e pilotos
equipes = {
    "LUCAS DI GRASSI": "ABT CUPRA FORMULA E TEAM",
    "ROBIN FRIJNS": "ENVISION RACING",
    "DAN TICKTUM": "ERT FORMULA E TEAM"
}

vitorias = [14, 16, 2]
pilotos = list(equipes.keys())  # Lista com os nomes dos pilotos

# Definindo voltas e condições de corrida
num_voltas = 10  # Número de voltas da corrida
condicoes_climaticas = ["Ensolarado", "Chuvoso", "Nublado", "Nevando"]
condicao_atual = random.choice(condicoes_climaticas)  # Escolhe uma condição climática aleatória dentro da lista
tamanho_circuito = 3  # Tamanho do circuito em km

# Função para simular a velocidade de cada piloto em cada volta
def simular_volta(piloto, velocidades_pilotos):
    # Calcula a distância percorrida em segundos
    distancia_percorrida = ((tamanho_circuito / velocidades_pilotos[piloto]) * 3600)
    return distancia_percorrida  # Retorna o tempo formatado

# Iniciando a simulação
print('BEM-VINDO AO NOSSO JOGO DE APOSTAS!!!!!')
print("Durante a corrida de hoje o clima está:", condicao_atual)

# Determina os favorecidos e desfavorecidos com base na condição climática
if condicao_atual == "Ensolarado":
    favorecido = desfavorecido = None
    print("O clima não desfavorece nenhuma equipe!")
    print("\nMultiplicadores de vitória:")
    print("Todos os pilotos: 1.5X")
elif condicao_atual == "Chuvoso":
    favorecido = "DAN TICKTUM"
    desfavorecido = "LUCAS DI GRASSI"
    print("O clima desfavoreceu a equipe: ABT CUPRA FORMULA E TEAM")
    print("O clima favoreceu a equipe: ERT FORMULA E TEAM")
    print("\nMultiplicadores de vitória:")
    print("LUCAS DI GRASSI (ABT CUPRA FORMULA E TEAM): 2.0X")
    print("ROBIN FRIJNS (ENVISION RACING): 1.5X")
    print("DAN TICKTUM (ERT FORMULA E TEAM): 1.2X")
elif condicao_atual == "Nublado":
    favorecido = "LUCAS DI GRASSI"
    desfavorecido = "ROBIN FRIJNS"
    print("O clima desfavoreceu a equipe: ENVISION RACING")
    print("O clima favoreceu a equipe: ABT CUPRA FORMULA E TEAM")
    print("\nMultiplicadores de vitória:")
    print("LUCAS DI GRASSI (ABT CUPRA FORMULA E TEAM): 1.2X")
    print("ROBIN FRIJNS (ENVISION RACING): 2.0X")
    print("DAN TICKTUM (ERT FORMULA E TEAM): 1.5X")
elif condicao_atual == "Nevando":
    favorecido = "ROBIN FRIJNS"
    desfavorecido = "DAN TICKTUM"
    print("O clima desfavoreceu a equipe: ERT FORMULA E TEAM")
    print("O clima favoreceu a equipe: ENVISION RACING")
    print("Multiplicadores de vitória:")
    print("LUCAS DI GRASSI (ABT CUPRA FORMULA E TEAM): 1.5X")
    print("ROBIN FRIJNS (ENVISION RACING): 1.2X")
    print("DAN TICKTUM (ERT FORMULA E TEAM): 2.0X")

# Exibe os pilotos disponíveis para aposta e suas equipes
print("\nPilotos disponíveis para aposta:")
for piloto, equipe in equipes.items():
    print(f"{piloto} - {equipe}")

# Solicita ao jogador que faça sua aposta
piloto_apostado = input("Em qual piloto você deseja apostar?: ").upper()
valor_apostado = float(input("Quanto você deseja apostar?: "))

# Dicionário para armazenar o tempo total de cada piloto
tempos_pilotos = {piloto: 0 for piloto in pilotos}

# Simulação das voltas da corrida
for volta in range(1, num_voltas + 1):  # O for garante que o range está dentro do número de voltas estipulado
    # Define as velocidades dos pilotos com base na condição climática
    if condicao_atual == "Ensolarado":
        velocidades_pilotos = {
            "LUCAS DI GRASSI": random.randint(150, 322),  # O comando "random.randint" escolhe um valor aleatório entre 150 e 322
            "ROBIN FRIJNS": random.randint(150, 322),
            "DAN TICKTUM": random.randint(150, 322)
        }
    elif condicao_atual == "Chuvoso":
        velocidades_pilotos = {
            "LUCAS DI GRASSI": random.randint(135, 310),
            "ROBIN FRIJNS": random.randint(150, 322),
            "DAN TICKTUM": random.randint(175, 322)
        }
    elif condicao_atual == "Nublado":
        velocidades_pilotos = {
            "LUCAS DI GRASSI": random.randint(175, 322),
            "ROBIN FRIJNS": random.randint(135, 310),
            "DAN TICKTUM": random.randint(150, 322)
        }
    elif condicao_atual == "Nevando":
        velocidades_pilotos = {
            "LUCAS DI GRASSI": random.randint(150, 322),
            "ROBIN FRIJNS": random.randint(175, 322),
            "DAN TICKTUM": random.randint(135, 320)
        }
    
    print(f" Volta {volta}/{num_voltas}")

    # Calcula o tempo de cada piloto para a volta atual
    for piloto in pilotos:
        tempo_volta = simular_volta(piloto, velocidades_pilotos)
        tempos_pilotos[piloto] += tempo_volta  # Acumula o tempo de cada volta no total de cada piloto
        print(f"{piloto} completou a volta em {tempo_volta:.2f} segundos, velocidade do piloto: {velocidades_pilotos[piloto]} km/h")
    print("-----------------------------------------------------------")

# Calcula a média de tempo de cada piloto
medias_pilotos = {piloto: tempos_pilotos[piloto] / num_voltas for piloto in pilotos}

# Determina o vencedor com a menor média de tempo
vencedor = min(medias_pilotos, key=medias_pilotos.get)
print("\nRESULTADO FINAL:")
for piloto, media_tempo in medias_pilotos.items():
    print(f"{piloto} teve uma média de {media_tempo:.2f} segundos por volta.")

print(f"\nO vencedor é {vencedor} com a menor média de tempo por volta!")

# Determina o multiplicador com base na condição do clima
if vencedor == favorecido:
    multiplicador = 1.2
elif vencedor == desfavorecido:
    multiplicador = 2.0
else:
    multiplicador = 1.5

# Calcula o prêmio do jogador
if piloto_apostado == vencedor:
    premio = valor_apostado * multiplicador
    print(f"Parabéns! Você apostou no vencedor {vencedor}!")
    print(f"Seu prêmio é: R${premio:.2f} (Multiplicador: {multiplicador}X)")
else:
    print(f"Você apostou em {piloto_apostado}, mas o vencedor foi {vencedor}.")
    print("Infelizmente, você perdeu sua aposta.")
```

## Exemplo de uso

```plaintext
BEM-VINDO AO NOSSO JOGO DE APOSTAS!!!!!

Durante a corrida de hoje o clima está: Chuvoso

O clima desfavoreceu a equipe: ABT CUPRA FORMULA E TEAM
O clima favoreceu a equipe: ERT FORMULA E TEAM

Multiplicadores de vitória:
LUCAS DI GRASSI (ABT CUPRA FORMULA E TEAM): 2.0X
ROBIN FRIJNS (ENVISION RACING): 1.5X
DAN TICKTUM (ERT FORMULA E TEAM): 1.2X

Pilotos disponíveis para aposta:
LUCAS DI GRASSI - ABT CUPRA FORMULA E TEAM
ROBIN FRIJNS - ENVISION RACING
DAN TICKTUM - ERT FORMULA E TEAM

Em qual piloto você deseja apostar?: DAN TICKTUM
Quanto você deseja apostar?: 100

Volta 1/10
LUCAS DI GRASSI completou a volta em 37.50 segundos, velocidade do piloto: 190 km/h
ROBIN FRIJNS completou a volta em 32.14 segundos, velocidade do piloto: 222 km/h
DAN TICKTUM completou a volta em 30.65 segundos, velocidade do piloto: 233 km/h

Volta 2/10
LUCAS DI GRASSI completou a volta em 35.30 segundos, velocidade do piloto: 200 km/h
ROBIN FRIJNS completou a volta em 33.25 segundos, velocidade do piloto: 215 km/h
DAN TICKTUM completou a volta em 31.45 segundos, velocidade do piloto: 228 km/h

...

Volta 10/10
LUCAS DI GRASSI completou a volta em 34.85 segundos, velocidade do piloto: 202 km/h
ROBIN FRIJNS completou a volta em 32.70 segundos, velocidade do piloto: 219 km/h
DAN TICKTUM completou a volta em 30.90 segundos, velocidade do piloto: 232 km/h

RESULTADO FINAL:
LUCAS DI GRASSI teve uma média de 36.80 segundos por volta.
ROBIN FRIJNS teve uma média de 32.40 segundos por volta.
DAN TICKTUM teve uma média de 30.75 segundos por volta.

O vencedor é DAN TICKTUM com a menor média de tempo por volta!

Parabéns! Você apostou no vencedor DAN TICKTUM!
Seu prêmio é: R$120.00 (Multiplicador: 1.2X)

```


