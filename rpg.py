from time import sleep #import para delay
delay = 1 #definição do tempo de delay

#ESCOLHA DA CLASSE-------------------------------------------------------------------------------------------------------------------------------------------------------------
classe = input("escolha sua classe: Guerreiro, Mago ou Ladino (escreva igual com a primeira letra maiúscula): ")

while classe != 'Guerreiro' and classe != 'Mago' and classe != 'Ladino': 
    classe = input("escolha sua classe: Guerreiro, Mago ou Ladino (escreva igual com a primeira letra maiúscula): ") 

#DEFINIR VALORES DE VIDA E MANA COM BASE NA CLASSE
if classe == 'Guerreiro':
    vidaMax = 200
    manaMax = 50
elif classe == 'Mago':
    vidaMax = 50
    manaMax = 200
elif classe == 'Ladino':
    vidaMax = 100
    manaMax = 100

#MOSTRAR A CLASSE E OS VALORES  
print(f'Sua classe é {classe} sua vida é {vidaMax} e sua mana é {manaMax}')

sleep(delay)#delay

#ESCOLHA DA HABILIDADE DA CLASSE------------------------------------------------------------------------------------------------------------------------------------------------
habilidadeClasse = 'undefined'#faz com que inicialmente seja indefinido a variável habilidadeClasse
if classe == 'Guerreiro':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para fúria (aumento de vida e dano em 30% por e rodadas), digite 2 para golpe desleal (30 de dano físico) ou digite 3 para revigorância (recupera instantaneamente 50 de vida, ultrapassando o valor base): ")
elif classe == 'Mago':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para bola de fogo (30 de dano mágico), digite 2 para raio (10 de dano mágico e ganha mais um turno) ou digite 3 para véu mágico (sofre 30% menos de dano por 3 rodadas): ")
elif classe == 'Ladino':
    while habilidadeClasse != '1' and habilidadeClasse != '2' and habilidadeClasse != '3': 
        habilidadeClasse = input("Escolha sua habilidade de classe, digite 1 para roubo (roube 20 de vida do adversário), digite 2 para astúcia (por 5 turnos você terá 1/4 de chance de desviar do ataque) ou digite 3 para ataque surpresa (30 de dano físico): ")

sleep(delay)#delay    

#MOSTRAR AO USUÁRIO A HABILIDADE ESCOLHIDA
#GUERREIRO
if classe == 'Guerreiro' and habilidadeClasse == '1':
    habilidadeClasse = 'fúria'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif classe == 'Guerreiro' and habilidadeClasse == '2':
    habilidadeClasse = 'golpe desleal'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif classe == 'Guerreiro' and habilidadeClasse == '3':
    habilidadeClasse = 'revigorância'
    print(f'Sua habilidade é {habilidadeClasse}')
#MAGO
elif classe == 'Mago' and habilidadeClasse == '1':
    habilidadeClasse = 'bola de fogo'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif classe == 'Mago' and habilidadeClasse == '2':
    habilidadeClasse = 'raio'
    print(f'Sua habilidade é {habilidadeClasse}')
elif classe == 'Mago' and habilidadeClasse == '3':
    habilidadeClasse = 'véu mágico'
    print(f'Sua habilidade é {habilidadeClasse}')
#LADINO
elif classe == 'Ladino' and habilidadeClasse == '1':
    habilidadeClasse = 'roubo'
    print(f'Sua habilidade é {habilidadeClasse}') 
elif classe == 'Ladino' and habilidadeClasse == '2':
    habilidadeClasse = 'astúcia'
    print(f'Sua habilidade é {habilidadeClasse}')
elif classe == 'Ladino' and habilidadeClasse == '3':
    habilidadeClasse = 'ataque surpresa'
    print(f'Sua habilidade é {habilidadeClasse}')