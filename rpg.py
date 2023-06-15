#ESCOLHA DA CLASSE
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
