# Evan Zhang
# 1/13/2021
# Boggle Solver

import random
from nltk.corpus import words
import nltk
nltk.download('words')

def findWords(i, j, board, visited, word):
    word_list = []
    visited[i][j] = True
    word += board[i][j]
    # print(word.lower())
    if len(word) > 2:
        # print(word.lower())
        if word.lower() in words.words():
            word_list.append(word)
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if row < len(board) and col < len(board):
                if row >= 0 and col >= 0 and not visited[row][col]:
                    # print(board[row][col], end=" ")
                    # for u in visited:
                    #     print(u)
                    word_list.extend(findWords(row, col, board, visited, word))
    word = word[:-1]
    visited[i][j] = False
    return word_list


# Check all combinations of strings and return array of 
def solveBoggle(board):
    visited = []
    solutions = []
    for i in range(len(board)): 
        column = [] 
        for j in range(len(board)): 
            column.append(False) 
        visited.append(column)

    for i in range(len(board)):
        for j in range(len(board)):
            print("starts with", board[i][j])
            solutions.append(findWords(i, j, board, visited, ""))            
    return solutions


def makeBoard(board_size):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    board = [] 
    for i in range(board_size): 
        column = [] 
        for j in range(board_size): 
            column.append(random.choice(alphabet)) 
        board.append(column) 
    return board


# Game Loop
def runBoggle(board_size):
    print("\n\nStarting game...")
    points = 0
    board = makeBoard(board_size)
    # board = [['G', 'I', 'Z'], ['U','E','K'], ['Q','S','E']]
    board = [['M','O'], ['M', 'O']]
    correct_user_words = []
    solutions = solveBoggle(board)
    while len(solutions) == 0:
        print("Bad board, making new one...")
        board = makeBoard(board_size)
        solutions = solveBoggle(board)
    print("\n----- Rules -----")
    print("Create words using adjacent cells.\nNo repeating the same cell.")
    print("Words must be at least 3 letters long")
    print("Every word worth is worth 1 point + any letters after the 3rd letter\n")
    while True:
        print()
        for i in board:
            print(i, sep=" ")
        print("Points: ", points)
        user_input = input("Enter a word, w - solve boggle, q - quit game: ")
        if user_input == 'w':
            print("All possible words:")
            for i in solutions:
                print(i)
            print("\nFinal Score: ", points)
            break
        elif user_input == 'q':
            print("\nFinal Score: ", points)
            break
        else:
            user_input = user_input.upper()
            if len(user_input) < 3:
                print("Word must be 3 or more letters long")
            elif user_input in correct_user_words:
                print("You have already found this word!")
            else:
                if user_input in solutions:
                    print(user_input, "accepted")
                    correct_user_words.append(user_input)
                    solutions.remove(user_input)
                    points += 1 + (len(user_input) - 3)
                    if len(solutions) == 0:
                        print("You have solved the Boggle!")
                        print("\nFinal Score: ", points)
                        break   
                else:
                    print(user_input, "not found on this board")
        

# Main Menu
def main():
    print("\n----- Boggle -----")
    board_size = 4
    while True:
        user_input = input("\nw - start game, e - edit board size, q - quit: ")
        if user_input == 'w':
            runBoggle(board_size)
            pass
        elif user_input == 'e':
            while True:
                board_size = input('Enter new board size: ')
                if board_size.isdigit() and int(board_size) > 1:
                    print("board size =", board_size)
                    board_size = int(board_size)
                    break
                else:
                    print("Please enter an integer greater than 1")
        elif user_input == 'q':
            print("\nGoodbye!\n")
            break
        else:
            print(user_input, "is not an option.")
        

if __name__ == "__main__":
    main()