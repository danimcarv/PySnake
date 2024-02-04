import numpy as np

tela = np.zeros((20,20))

#def preencheMatriz(matriz, dimensao) :
#    for i in range(dimensao) :
#        for j in range(dimensao) :
#            matr

#def criaTela(matriz, dimensao) :
    
#    for coluna in range(dimensao-1) :
#        for linha in range(dimensao-1) :
#            if coluna == linha :
#                matriz[coluna][linha] = 1

#        matriz[index][0] = 1
#        matriz[index][(dimensao-1)] = 1
#        matriz[0][index] = 1
#        matriz[(dimensao-1)][index] = 1

#criaTela(tela, 20)

for i in range(20) :
    tela[i, 0] = 1

for i in range(20) :
    tela[0, i] = 1

for i in range(20) :
    tela[i, 19] = 1

for i in range(20) :
    tela[19, i] = 1

print(tela)

print("\n\n")

for i in range(20) :
    print(" ")
    for j in range(20) :
        if tela[i, j] == 1 :
            print("#", end="")
        elif tela[i, j] == 0 :
            print(" ", end="")
        else :
            print(str(tela[i, j]), end="")
#    print("\n")



