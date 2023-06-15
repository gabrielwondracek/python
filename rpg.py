import random #import para randomizar números
from time import sleep #import para delay
delay = 1 #definição do tempo de delay para 1 segundos
delay2 = 2 #definição do tempo de delay para 2 segundos

#ESCOLHA DA CLASSE-------------------------------------------------------------------------------------------------------------------------------------------------------------
classe = 'undefined'#faz com que inicialmente seja indefinido a variável classe
confirmacaoClasse = 'undefined'#faz com que inicialmente seja indefinido a variável confirmacaoClasse

while classe != 'Guerreiro' and classe != 'Mago' and classe != 'Ladino': 
    classe = input("escolha sua classe: Guerreiro, Mago ou Ladino (escreva igual com a primeira letra maiúscula): ")

#DEFINIR VALORES DE VIDA E MANA COM BASE NA CLASSE
if classe == 'Guerreiro':
    vidaMax = 250
    defesaFisica = 0.8
    defesaMagica = 0.8
elif classe == 'Mago':
    vidaMax = 100
    defesaFisica = 0.95
    defesaMagica = 0.95
elif classe == 'Ladino':
    vidaMax = 150
    defesaFisica = 0.9
    defesaMagica = 0.9

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

#ESCOLHA DO EQUIPAMENTO------------------------------------------------------------------------------------------------------------------------------------------------
equipamento = 'undefined'#faz com que inicialmente seja indefinido a variável habilidadeClasse
if classe == 'Guerreiro':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 para espada longa (40 de dano físico), digite 2 para espada e escudo (25 de dano físico e sofre 20% menos de dano): ")
elif classe == 'Mago':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 para cajado mágico (40 de dano mágico), digite 2 para adaga mágica (25 de dano mágico e 15 de dano físico): ")
elif classe == 'Ladino':
    while equipamento != '1' and equipamento != '2': 
        equipamento = input("Escolha seu equipamento, digite 1 rapieira (30 de dano físico e 1/4 de chance de duplicar o dano), digite 2 para bastão (20 de dano físico e 1/4 de chance de atordoar o inimigo por 1 turno): ")

sleep(delay)#delay 

#MOSTRAR AO USUÁRIO O EQUIPAMENTO ESCOLHIDO
#GUERREIRO
if classe == 'Guerreiro' and equipamento == '1':
    equipamento = 'espada longa'
    danoFisico = 40
    danoMagico = 0
elif classe == 'Guerreiro' and equipamento == '2':
    equipamento = 'espada e escudo'
    danoFisico = 25
    danoMagico = 0
    defesaFisica = defesaFisica - 0.2
    defesaMagica = defesaMagica - 0.2
#MAGO
elif classe == 'Mago' and equipamento == '1':
    equipamento = 'cajado mágico'
    danoFisico = 0
    danoMagico = 40
elif classe == 'Mago' and equipamento == '2':
    equipamento = 'adaga mágica'
    danoFisico = 15
    danoMagico = 25
#LADINO
elif classe == 'Ladino' and equipamento == '1':
    equipamento = 'rapieira'
    danoFisico = 30
    danoMagico = 0 
elif classe == 'Ladino' and equipamento == '2':
    equipamento = 'bastão'
    danoFisico = 20
    danoMagico = 0 
    atordoamento = '0'
print(f'Seu equipamento é {equipamento}')

sleep(delay2)#delay

#FALAR TODOS OS ATRIBUTOS------------------------------------------------------------------------------------------------------------------------------------------------
print(f'Sua classe é {classe} sua vida é {vidaMax} sua habilidade é {habilidadeClasse} e seu equipamento é {equipamento}')

sleep(delay2)#delay

#ESCOLHA ALEATÓRIA DO INIMIGO--------------------------------------------------------------------------------------------------------------------------------------------
inimigo = random.randint(1,4) #faz a variável inimigo ter um valor entre 1 a 4

#Goliath
if inimigo == 1:
    inimigo = 'Goliath'
    vidaInimigo = random.randint(350,800)
    danoInimigo = random.randint(5,10)
    defesaFisicaInimigo = 0.9
    defesaMagicaInimigo = 0.9
    habilidadeInimigo = 'Dureza' #sofre 55% menos dano por 3 turnos
#Caçador de mago
if inimigo == 2:
    inimigo = 'Caçador de mago'
    vidaInimigo = random.randint(30,70)
    danoInimigo = random.randint(10,35)
    defesaFisicaInimigo = 1.2
    defesaMagicaInimigo = 0.1
    habilidadeInimigo = 'Caçar magia' #o usuário não poderá mais utlizar habilidade
#Mago antigo
if inimigo == 3:
    inimigo = 'Mago antigo'
    vidaInimigo = random.randint(15,60)
    danoInimigo = random.randint(25,30)
    defesaFisicaInimigo = 0.2
    defesaMagicaInimigo = 1.2
    habilidadeInimigo = 'Bola elétrica' #causa 50 de dano e ignora a defesa mágica
#Guerreiro de pedra
if inimigo == 4:
    inimigo = 'Guerreiro de pedra'
    vidaInimigo = random.randint(115,600)
    danoInimigo = random.randint(7,15)
    defesaFisicaInimigo = 0.8
    defesaMagicaInimigo = 0.8
    habilidadeInimigo = 'Petrificar' #pula um turno do usuário
print(f'Seu inimigo é {inimigo} com vida de {vidaInimigo} dano de {danoInimigo} e sua habilidade é {habilidadeInimigo}') #falar o inimigo e seus atributos

#BATALHA------------------------------------------------------------------------------------------------------------------------------------------------
turno = 1 #define o turno inicial como 1
while vidaInimigo >= 0 or vidaMax >= 0:

    chanceAtordoar = random.randint(1,4)
    if chanceAtordoar == 1: #if para verificar se o ataque vai atordoar
       danoFisico = 20
       danoMagico = 0 
       atordoamento = '1'
    else:
        danoFisico = 20
        danoMagico = 0 
        atordoamento = '0'

    chanceDeCritar = random.randint(1,4)
    if chanceDeCritar == 1: #if para verificar se o ataque foi crítico
       danoFisico = 60
       danoMagico = 0 
    else:
        danoFisico = 30
        danoMagico = 0 
    
    print(f'Fim do {turno} turno!')
    turno = turno + 1