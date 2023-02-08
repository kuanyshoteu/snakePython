# 10 X 10
# 1. Вывод двумерного массива заполненного точками '.'
# 2. Создаем рандомные координаты для змейки snakeX snakeY
# 3. В этих координатах сохранить '>' //'v' '<' '^'
# 4. Также появляется яблоко "0"
# 5. Съедает яблоко - яблоко исчезает и появляется в другом рандомном месте
# 6. Змейка растет
import random
width = 10
height = 10
field = []

appleX=0
appleY=0
snakeLength = 1
snakeX = random.randint(1, 9)
snakeY = random.randint(1, 9)
diriction = 'd'

def clearField():
    field.clear()
    for i in range(height):
        row = ''
        for j in range(width):
            row+='.'
        field.append(list(row))
        row = ''  
def saveSnake():
    print("saveSnake")
    global field, diriction, snakeX, snakeY
    print(diriction)
    if(diriction == 'w'):
        field[snakeY][snakeX] = '^'
        for i in range(snakeLength):
            field[snakeY+i][snakeX] = '#'
    if(diriction == 'd'):
        field[snakeY][snakeX] = '>'
        field[snakeY][snakeX-1] = '#'
    if(diriction == 'a'):
        field[snakeY][snakeX] = '<'
        field[snakeY][snakeX+1] = '#'
    if(diriction == 's'):
        print("S11")
        field[snakeY][snakeX] = 'v'
        field[snakeY-1][snakeX] = '#'

def saveApple():
    field[appleY][appleX] = '0'

def newApple(appleX):
    global appleX, appleY, snakeX, snakeY
    while((appleX == snakeX-1 or appleX == snakeX) and appleY == snakeY):
        appleX = random.randint(0, 9)
        appleY = random.randint(0, 9)

def drawField():
    global field, diriction, snakeX, snakeY
    for i in range(height):
        for j in range(width):
            print(field[i][j], end=' ')
        print('')

def moveSnake():
    global diriction, snakeX, snakeY
    diriction = input()
    if(diriction == 'd'):
        snakeX += 1
    if(diriction == 'a'):
        snakeX -= 1
    if(diriction == 'w'):
        snakeY -= 1
    if(diriction == 's'):
        snakeY += 1

while(True):
    clearField()
    saveSnake()
    newApple()
    saveApple()
    drawField()  
    moveSnake()