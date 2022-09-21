# i define first the grid


theGrid = {'1': ' ', '2': ' ', '3': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '7': ' ', '8': ' ', '9': ' '}

grid_keys = []

for key in theGrid:
    grid_keys.append(key)


def printGrid(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# here I define the moves
# the main function
def main():

    turn = 'X'
    count = 0

    for i in range(10):
        printGrid(theGrid)
        print("It's " + turn + "'s turn, " + turn + " Move to which place (1-9)? ")

        move = input()

        if theGrid[move] == ' ':
            theGrid[move] = turn
            count += 1

        else:
            print("That place is already filled.\nMove to which place (1-9)? ")
            continue

# I define here the conditions to define the winner
        if count >= 5:
            if theGrid['1'] == theGrid['2'] == theGrid['3'] != ' ':  # the top line
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['4'] == theGrid['5'] == theGrid['6'] != ' ':  # the middle line
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['7'] == theGrid['8'] == theGrid['9'] != ' ':  # the bottom line
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['1'] == theGrid['4'] == theGrid['7'] != ' ':  # the first  colomn
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['2'] == theGrid['5'] == theGrid['8'] != ' ':  # the second  colomn
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['3'] == theGrid['6'] == theGrid['9'] != ' ':  # the third  colomn
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['1'] == theGrid['5'] == theGrid['9'] != ' ':  # one diagonal
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

            elif theGrid['7'] == theGrid['5'] == theGrid['3'] != ' ':  # other diagonal
                printGrid(theGrid)
                print("\nGame Over.\n")
                print("******** " + turn + " won.********")
                break

# if no one of the player wins, the result is declared as tie
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break
# this is to change the player after every move
        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'

# this is to ask the players if they want to play again

    restart = input("Do you want to play again?(y/n)")

    
    while restart !="n" or restart !="N":
        
        if restart == "y" or restart == "Y":
            for key in grid_keys:
                theGrid[key] = " "
            main()
        
        elif restart =="n" or restart == "N":
            break
            
        else:
            print()
            print("please enter a correct value")
            restart = input("Do you want to play again?(y/n)")
            


if __name__ == "__main__":
    main()
