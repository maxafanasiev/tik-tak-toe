import os
import time
import re

def print_field():
    print("{:^13}".format("-"*13))
    for column in field.values():
        print("|{:^3}|{:^3}|{:^3}|".format(column[1],column[2],column[3],))
        print("{:^13}".format("-"*13))
    


clear = lambda: os.system('clear')


field = {1:['','','',''],
    2:['','','',''],
    3:['','','',''],
    }

def check():
    horisontal1 = (field[1].count('x') == 3 or field[1].count('o') == 3)
    horisontal2 = (field[2].count('x') == 3 or field[2].count('o') == 3)
    horisontal3 = (field[3].count('x') == 3 or field[3].count('o') == 3)

    vertical1 = (field[1][1] == field[2][1] == field[3][1] and field[1][1] != '')
    vertical2 = (field[1][2] == field[2][2] == field[3][2] and field[1][2] != '')
    vertical3 = (field[1][3] == field[2][3] == field[3][3] and field[1][3] != '')

    diagonal1 = ((field[1][1] == field[2][2] and field[1][1] == field[3][3]) and field[1][1] != '')
    diagonal2 = ((field[1][3] == field[2][2] and  field[1][3] == field[3][1]) and field[1][3] != '')

    diagonal = diagonal1 or diagonal2 
    vertical = vertical1 or vertical2 or vertical3 
    horisontal = horisontal1 or horisontal2 or horisontal3
    return diagonal or vertical or horisontal


def start():
    clear()
    print("{:^60}".format('Tic-Tac-Toe Game'))
    print("{:^60}".format('-'*60))
    print("{:^60}".format('Player1 - x | Player2 - o'))
    print("{:^60}".format('-'*60))
    print("{:^60}".format("Game starting"))
    time.sleep(3) 


def step(x):
        if x: 
            name = "Player 1"
            draw = 'x'
        else:
            name = "Player 2"
            draw = 'o'
        ch = False
        row = 1
        col = 0
        while not ch or field[row][col] in ('x', 'o'):
            try:
                step = input(f'{name} you turn. Print row/column (1,2,3).\n')
                ch = re.search('[1-3]{1}/[1-3]{1}', step)
                coord = step.split('/')
                row = int(coord[0])
                col = int(coord[1])
            except:
                print('Enter correct coords. */* ')
        field[row][col] = draw

def main():
    player = False
    while True:
        clear()
        if check():
            print('Player 1 win.' if player else 'Player 2 win.')
            break
        print_field()
        player = not player
        step(player)
            

        


if __name__ == '__main__':
    start()
    main()
