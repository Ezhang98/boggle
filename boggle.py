# Evan Zhang
# 1/13/2021
# Boggle Solver

import random

class Trie:
    def __init__(self, letter):
        self.branches = []
        self.letter = letter
        self.isLeaf = False


def trieInsert(root_node, word):
    node = root_node
    for letter in word:
        in_word = False
        for branch in node.branches:
            if branch.letter == letter:
                node = branch
                in_word = True
                break
        if in_word == False:
            new_node = Trie(letter)
            node.branches.append(new_node)
            node = new_node
    node.isLeaf = True


def findWords(i, j, board, visited, word, node, dic):
    word_list = []
    visited[i][j] = True
    in_trie = False
    temp = node
    for b in node.branches:
        if board[i][j] == b.letter:
            in_trie = True
            word += board[i][j]
            temp = b
    if in_trie == True:
        if len(word) > 2:
            if word in dic:
                word_list.append(word) 
        if not temp.isLeaf:
            for row in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):
                    if row < len(board) and col < len(board):
                        if row >= 0 and col >= 0 and not visited[row][col]:
                            word_list.extend(findWords(row, col, board, visited, word, temp, dic))
    word = word[:-1]
    temp = node
    visited[i][j] = False
    return word_list


def printTrie(root):
    if root.isLeaf:
        return
    for b in root.branches:
        print(b.letter, end=" ")
        printTrie(b)

# DFS checking using the trie to determine if word exists in dictionary
def solveBoggle(board, dic, trie):
    visited = []
    solutions = set()
    for i in range(len(board)): 
        column = [] 
        for j in range(len(board)): 
            column.append(False) 
        visited.append(column)

    for i in range(len(board)):
        for j in range(len(board)):
            solutions.update(findWords(i, j, board, visited, "", trie, dic))
                        
    return solutions


def makeBoard(board_size, dic):
    board = [] 
    for i in range(board_size): 
        column = [] 
        for j in range(board_size): 
            column.append(random.choice(random.choice(dic))) 
        board.append(column) 
    return board


# Game Loop
def runBoggle(board_size, trie, dic):
    print("\n\nStarting game...")
    points = 0
    board = makeBoard(board_size, dic)

    # example board
    # board = [['R','A', 'E', 'L'], ['M', 'O', 'F', 'S'], ['T', 'E', 'O', 'K'], ['N', 'A', 'T', 'I']]
    # dic = ["MEAT", "NEAT", "FOOT", "ROOK", "TOOK", "SEA", "ATE"]
    
    correct_user_words = []
    solutions = solveBoggle(board, dic, trie)

    while len(solutions) == 0:
        print("Bad board, making new one...")
        board = makeBoard(board_size, dic)
        solutions = solveBoggle(board, dic, trie)

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
            print("All other possible words:")
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
                    print("Sorry,", user_input, "not found in dictionary or not on board")
        

# Main Menu
def main():
    print("\n----- Boggle -----")
    board_size = 4
    dic = []
    dic_file = open("dictionary.txt", "r")
    while True:
        word = dic_file.readline()
        if len(word) == 0:
            break
        dic.append(word.strip().upper())
    
    root = Trie(None)
    for word in dic:
        trieInsert(root, word)


    while True:
        user_input = input("\nw - start game, e - edit board size, q - quit: ")
        if user_input == 'w':
            runBoggle(board_size, root, dic)
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