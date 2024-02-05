import numpy as np
import time
import os
if os.name=='nt' :
    import msvcrt
else :
    try :
        import sys
        import select
        import tty
        import termios
    except:
        print("Unsupported Operating System.")
        print("This game is only supported on Windows and Unix-like systems.")
        exit()

dimens = 30
interval = 0.1

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

snake = [9,9]

def snakeFill() :
    for i in range(0,len(snake),2) :
        x = snake[i]
        y = snake[i+1]
        if(tela[x,y]!=1) :
            tela[x,y]=2
        else :
            clearScreen()
            return("Collision")

direction = "right"

def pressedKeyNT() :
    # If an arrow key is pressed
    code1 = msvcrt.getch()
    if code1 == b'\xe0' :
        code2 = msvcrt.getch()
        # If up
        if code2 == b'H' :
            return "up"
        # If down
        elif code2 == b'P' :
            return "down"
        # If right
        elif code2 == b'M' :
            return "right"
        # If left
        elif code2 == b'K' :
            return "left"
    # If ESC key is pressed
    elif code1 == b'\x1b' :
        return "exit"

def directionChange(ret) :
    if (ret == "exit") :
        clearScreen()
        print("You pressed ESC\nExiting game")
        return "exit"
    else :
        global direction
        direction = ret
 
def movimentaSnake() :
    if direction == "down" :
        for i in range(0,len(snake),2) :
            snake[i] = snake[i]+1
    elif direction == "right" :
        for i in range(1,len(snake),2) :
            snake[i] = snake[i]+1
    elif direction == "up" :
        for i in range(0,len(snake),2) :
            snake[i] = snake[i]-1
    elif direction == "left" :
        for i in range(1,len(snake),2) :
            snake[i] = snake[i]-1

def snakeMoving() :
    clearScreen()
    print("Welcome to PySnake game")
    time.sleep(1.5)
    clearScreen()
    print("Control the snake with arrows")
    print("If you want to exit game, press ESC at anytime")
    time.sleep(2)
    clearScreen()
    while(True) :
        zeraMatriz()
        redefineTela()
        if (snakeFill()) == "Collision" :
            clearScreen()
            print("GAME OVER")
            break
        exibeTela()
        if os.name=='nt' :
            if msvcrt.kbhit():
                if (directionChange(pressedKeyNT())) == "exit" :
                    break
        else :
            if unixKeyPress() :
                if (directionChange(pressedKeyUnix())) == "exit" :
                    break
        movimentaSnake()
        time.sleep(interval)
        clearScreen()
    
snakeMoving()