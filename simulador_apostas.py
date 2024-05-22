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
    
    print(f"Volta {volta}/{num_voltas}")

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
