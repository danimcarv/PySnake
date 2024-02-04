import numpy as np
import time
import os

dimens = 20

tela = np.zeros((dimens,dimens))
snake = []

def zeraMatriz() :
    for i in range(len(tela)) :
        for j in range(len(tela)) :
            tela[i,j]=0

def clearScreen() :
    if os.name=='nt' :
        os.system('cls')
    else :
        os.system('clear')

def redefineTela() :
    for i in range(dimens) :
        tela[i, 0] = 1
    
    for i in range(dimens) :
        tela[0, i] = 1

    for i in range(dimens) :
        tela[i, (dimens-1)] = 1

    for i in range(dimens) :
        tela[(dimens-1), i] = 1

def exibeTela() :
    for i in range(dimens) :
        print("")
        for j in range(dimens) :
            if tela[i, j] == 1 :
                print("#", end=" ")
            elif tela[i, j] == 0 :
                print(" ", end=" ")
            elif tela[i, j] == 2 :
                print("█", end=" ")
            else :
                print("E", end=" ")
    print("\n")

snake.append(9)
snake.append(9)

def snakeFill() :
    for i in range(0,len(snake),2) :
        x = snake[i]
        y = snake[i+1]
        if(tela[x,y]!=1) :
            tela[x,y]=2
        else :
            moving = False
            clearScreen()
            return("Collision")

direction = "right"
moving = True

def movimentaSnake() :
    if direction == "down" :
        for i in range(0,len(snake),2) :
            snake[i] = snake[i]+1
    if direction == "right" :
        for i in range(1,len(snake),2) :
            snake[i] = snake[i]+1
    if direction == "up" :
        for i in range(0,len(snake),2) :
            snake[i] = snake[i]-1
    if direction == "left" :
        for i in range(1,len(snake),2) :
            snake[i] = snake[i]-1

def snakeMoving() :
    clearScreen()
    while(moving==True) :
        zeraMatriz()
        redefineTela()
        if (snakeFill()) == "Collision" :
            clearScreen()
            print("GAME OVER")
            break
        exibeTela()
        movimentaSnake()
        time.sleep(1)
        clearScreen()
    
snakeMoving()