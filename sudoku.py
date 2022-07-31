import pygame
import sys
import random

# initialisation commands
pygame.init()
pygame.font.init()
height = width = 450
cell_size = 50
dimension = height // cell_size
font = pygame.font.Font('freesansbold.ttf', 32)
score = font.render("SCORE", True, (0, 0, 0))

# game board
class Game:
    def __init__(self):
        self.board = [["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"],
        ["-", "-", "-", "-", "-", "-","-", "-", "-"]]
        
    def update_board(self, number):
        pass


# checking validity of the number
def check_number(board, row, col, number):
    # check if number is present in same row or col
    for i in range(dimension):
        if board[row][i] == number:
            return False
        if board[i][col] == number:
            return False
    # check if number is in the square 3 x 3
    r = (col // 3) * 3
    c = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[i+c][j+r] == number:
                return False

    return True


# generating random number
def generate_random_number():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number = random.choice(numbers)
    return number
        

# preparing the board (i.e. randomly genrating numbers on board)
def ques_board():
    game = Game()
    board = game.board
    for i in range(9):
        number = generate_random_number()
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if check_number(board, row, col, number):
            game.board[row][col] = number
        else:
            i-=1
    return board


board = ques_board()


# main function having input commands
def main():
    screen = pygame.display.set_mode((height, width))
    screen.fill((255, 255, 255))
    position = ()
    draw_board(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                row = location[0] // cell_size
                col = location[1] // cell_size
                position = (row, col)
                if position != ():
                    selected(screen, position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    enter_number("1", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_2:
                    enter_number("2", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_3:
                    enter_number("3", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_4:
                    enter_number("4", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_5:
                    enter_number("5", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_6:
                    enter_number("6", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_7:
                    enter_number("7", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_8:
                    enter_number("8", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_9:
                    enter_number("9", position, screen)
                    draw_board(screen)
                if event.key == pygame.K_BACKSPACE:
                    delete(position, screen)
        if win():
            victory = font.render("Victory!", True, (255, 0, 0))
            screen.blit(victory, (225, 240))
        pygame.display.update()


# making the sudoku board
def draw_board(screen):
    screen.fill((255, 255, 255))
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == "-":
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(cell_size*i, cell_size*j, cell_size, cell_size))
            if board[i][j] != "-":
                selected_number = font.render(board[i][j], True, (0, 0, 0))
                screen.blit(selected_number, (cell_size * i + 20, cell_size * j + 10))
    for i in range(dimension + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, cell_size*i), (500, cell_size*i))
        pygame.draw.line(screen, (0, 0, 0), (cell_size*i, 0), (cell_size*i, 500))
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, cell_size*i*3), (500, cell_size*i*3), 5)
        pygame.draw.line(screen, (0, 0, 0), (cell_size*i*3, 0), (cell_size*i*3, 500), 5)


# enters number to the position selected
def enter_number(number, position, screen):
    i = position[0]
    j = position[1]
    if board[i][j] == "-" and check_number(board, i, j, number):
        num = font.render(number, True, (0, 0, 0))
        screen.blit(num, (cell_size*i + 20, cell_size*j + 10)) 
        board[i][j] = number


# delete the number from given position
def delete(position, screen):
    board[position[0]][position[1]] = "-"
    draw_board(screen)


# highlights selected square
def selected(screen, position):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(cell_size*position[0], cell_size*position[1], cell_size, cell_size), 2)


# checks if all blocks are occupied and return true and false accordingly
def win():
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == "-":
                return False
            else:
                continue
    return True


if __name__ == '__main__':
    main()
