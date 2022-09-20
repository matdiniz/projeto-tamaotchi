#tamagoshi Lili
#comer, dormir/acordar
#acordar é válido comer, e dormir
#dormir não é válido comer

import time as tm

statusFome = 8
statusDormindo = False
status = 9
comida = 0

print("\n" * 130)
tm.sleep(1.5)
print("Carregando Lili... ")
tm.sleep(3.5)
print("\n" * 130)
tm.sleep(1.3)
print("\nOlá eu sou a Lili, sua amiga virtual ^.^")
tm.sleep(1.7)


def liliDormir():  #Função de DORMIR
    global statusDormindo, statusFome
    statusDormindo = True  #Troca o status de dormir para True
    statusFome = statusFome - 1
    tm.sleep(0.5)
    print("Dormindo... >.< zZz")
    tm.sleep(4.0)

def liliComer():   #Função de ALIMENTAR
    global statusFome
    comidadisp = 10
    fome = comidadisp - statusFome
    print(f"Fome: [ {statusFome} / 10 ]")
    print(f"Só é possível alimentar até {fome}")
    print(f"Quanto deseja alimentar? [ 1 a {fome} ]")
    comida = int(input(": "))

    # teste de possibilidade para alimentar

    if comida <= 0:
        print("Não é possível alimentar só isso   ;.;")
    elif comida > fome:
        print(f"Só é possível alimentar até {fome}")
    elif comida <= fome:
        tm.sleep(2)
        print("\n... -.-")
        tm.sleep(1.5)
        print("*) ^.^ (*")
        statusFome = statusFome + comida
        tm.sleep(0.7)
        print("\nLili foi alimentada com sucesso!")
        tm.sleep(0.7)

def liliAcordar():   #Função de Acordar
    global statusDormindo, statusFome
    statusDormindo = False  #Troca o status de dormir para False
    statusFome = statusFome - 2
    tm.sleep(2)
    print("\n*Acordando Lili...* -.-")
    tm.sleep(1.5)
    print("... o.o")
    tm.sleep(0.7)
    print("Acordada ^.^")
    tm.sleep(0.7)

while status == 9:
    
    print("\n[1] DORMIR")
    tm.sleep(0.7)
    
    print("[2] ACORDAR")
    tm.sleep(0.7)

    print("[3] ALIMENTAR")
    tm.sleep(0.7)

    print("[0] Para desligar")
    tm.sleep(0.7)
    
    print(f"Meu status de fome: [{statusFome} / 10]")

    #verificação: Fome da Lili
    
    if statusFome <= 0:
        print("\nLili morreu! x.x")
        status = input("Aperte qualquer tecla para desligar Lili... ")
        status = 0
    elif statusFome < 2:
        print("\nEstou com fome... -_-")
        print("\n*Alimente Lili para que não morra*")
    elif statusFome < 4:
        print("\nHora de me alimentar -.-")
    elif statusFome < 5:
        print("\n*Não deixe Lili ficar com fome!*") 

    tm.sleep(0.7)
    status = input("\nO que deseja fazer: ")

    #bloco de ações Lili

    #if status != "1" or status != "2" or status != "3" or status != "4":
    #    print("\n\nNão entendi...   o.õ (?)  ")
    #    print("Tenta de novo ")
    #    status = 9

    if status == "1":    #Seleção da ação Dormir
        if statusDormindo == False: 
            liliDormir()
            status = 9
        else:
            tm.sleep(0.7)
            print("\nLili já está dormindo >.< zZz")
            tm.sleep(0.7)
            print("Para acorda-la, pressione [2]")
            statusFome = statusFome - 1
            status = 9

    if status == "2":   #Seleção da ação Acordar
        if statusDormindo == True:
            liliAcordar()
            status = 9
        else:           #Caso já esteja Acordada
            tm.sleep(0.7)
            statusFome = statusFome - 1
            print("\nLili já está acordada ^.^") 
            print("Para alimenta-la, pressione [3]. Ou para fazer ela dormir, pressione [1]")
            status = 9

    if status == "3":   #Seleção de comer
        if statusDormindo == True:
            tm.sleep(0.7)
            statusFome = statusFome - 1
            print("\nÉ preciso acordar Lili para alimentar. >.<")
            print("Para acorda-la, pressione [2]")
            status = 9
        elif statusDormindo == False: #teste para Fome caso esteja completa
        
            if statusFome == 10: 
                tm.sleep(0.7)
                print("\nNão é necessário comer agora. ~.~")
                status = 9
            elif statusFome > 0:
                liliComer()
                status = 9
    
    if status == "0":
        print("\nDeseja mesmo desligar? ")
        print("[S] para Sair")
        print("[N] para Voltar")
        status = input()
        if status == "N" or status == "n":
            status = 9
            print("Que bom que voltou ^.^")
        elif status == "s" or "S":
            status = 0

tm.sleep(1.7)
print("\n" * 130)
print("Desligando...")
tm.sleep(2.4)