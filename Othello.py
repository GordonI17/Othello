import copy

GameState = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "X", "O", 0, 0, 0],
             [0, 0, 0, "O", "X", 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

CurrentPlayer = "O"

print()
print("Welcome to Othello you will be 'O's for this game.")
print("To make your move you will be prompted with 'It's your turn', ")
print("and you will enter the cordinates if your next move selection in the order XY")
print()


def score(game, player):
    score = 0
    for y in game:
        for x in y:
            if(x == player):
                score = score + 1
    return score


def Gameboard(game):
    i = 1
    print("    1    2    3    4    5    6    7    8")
    for y in game:
        print(i, end=" ")
        for x in y:
            if(x != 0):
                print("| " + x + " ", end=" ")
            else:
                print("|   ", end=" ")
        print("|")
        print("  -----------------------------------------")
        i = i + 1
    print("Player's score: " + str(score(game, "O")))
    print("AI's score: " + str(score(game, "X")))
    return

#this will check for legal moves when input
def LegalMove(game, coordinate, player):
    x = int(coordinate / 10)
    y = coordinate - (x * 10)
    # check bounds
    if (x > 7 or x < 0 or y > 7 or y < 0):
        return None
    # check if place is already taken
    if (game[y][x] == "X" or game[y][x] == "O"):
        return None
    temp = copy.deepcopy(game)
    test = copy.deepcopy(game)
    # up
    if (y != 0):
        i = 1
        while(y - i >= 0):
            if (game[y - i][x] == player):
                break
            elif (game[y - i][x] != 0 and y - i > 0):
                temp[y - i][x] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # up-left
    if (y != 0 and x != 0):
        i = 1
        while(y - i >= 0 and x - i >= 0):
            if (game[y - i][x - i] == player):
                break
            elif (game[y - i][x - i] != 0 and y - i > 0 and x - i > 0):
                temp[y - i][x - i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # left
    if (x != 0):
        i = 1
        while(x - i >= 0):
            if (game[y][x - i] == player):
                break
            elif (game[y][x - i] != 0 and x - i > 0):
                temp[y][x - i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # left-down
    if (y <= 6 and x > 0):
        i = 1
        while(x - i >= 0 and y + i <= 7):
            if (game[y + i][x - i] == player):
                break
            elif (game[y + i][x - i] != 0 and x - i > 0 and y + i < 7):
                temp[y + i][x - i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # down
    if (y != 7):
        i = 1
        while (y + i <= 7):
            if (game[y + i][x] == player):
                break
            elif (game[y + i][x] != 0 and y + i < 7):
                temp[y + i][x] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # down-right
    if (y <= 6 and x <= 6):
        i = 1
        while(x + i <= 7 and y + i <= 7):
            if (game[y + i][x + i] == player):
                break
            elif (game[y + i][x + i] != 0 and x + i < 7 and y + i < 7):
                temp[y + i][x + i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # right
    if (x != 7):
        i = 1
        while(x + i <= 7):
            if (game[y][x + i] == player):
                break
            elif (game[y][x + i] != 0 and x + i < 7):
                temp[y][x + i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    # right-up
    if (y != 0 and x <= 7):
        i = 1
        while(x + i <= 7 and y - i >= 0):
            if (game[y - i][x + i] == player):
                break
            elif (game[y - i][x + i] != 0 and x + i < 7 and y - i > 0):
                temp[y - i][x + i] = player
            else:
                temp = copy.deepcopy(game)
                break
            i = i + 1
        game = copy.deepcopy(temp)
    #all changes to the board are made besides the in question move
    if(temp == test):
        return
    else:
        return game


def MakeMove(game, coordinate, player):
    game = LegalMove(game, coordinate, player)
    x = int(coordinate / 10)
    y = coordinate - (x * 10)
    game[y][x] = player
    return game


# possible add in later to show people their possible moves
def possibleMoves(game, player):
    x = 0
    i = 0
    possible = []
    while (x <= 7):
        y = 0
        while(y <= 7):
            temp = LegalMove(game, (x * 10) + y, player)
            if(temp != None and temp != game):
                possible.append((x * 10) + y)
            y = y + 1
            i = i + 1
        i = i + 1
        x = x + 1
    return possible


#Called to start the game
def Start(Game):
    moves = []
    while(1):
        madeMove = False
        moves = possibleMoves(Game, "O")
        Gameboard(Game)
        if (len(moves) == 0):
            for y in Game:
                for x in y:
                    if(x == 0):
                        print("you have run out of moves, and lost")
                        return
            print("the game has ended, and the final scores are:")
            print("Player's score: " + str(score(Game, "O")))
            print("AI's score: " + str(score(Game, "X")))
            break
        i = 0
        for item in moves:
            moves[i] = item + 11
            i = i + 1
        while (not madeMove):
            print("valid moves: ", end=" ")
            print(moves)
            coordinate = int(input("enter your move: "))
            if (coordinate > 88):
                print("invalid choice")
            if (coordinate in moves):
                print("making move...")
                madeMove = True
                coordinate = coordinate - 11
                Game = MakeMove(Game, coordinate, "O")
                Gameboard(Game)
            else:
                print("this is not a valid move")
        print("the AI is making a decision...")
        Game = Agent(Game)


#player minimizes
def Min(game, a, b, iteration):
    iteration = iteration - 1
    moves = possibleMoves(game, "O")
    move = -100
    value = 10000
    if(iteration != 0):
        for item in moves:
            if(game != None):
                game = MakeMove(game, item, "O")
                nextValue, next = Max(game, a, b, iteration)
                if (value > nextValue):
                    value = nextValue
                    move = item
                    a = min(a, value)
                if (value >= b):
                    return value, move
    return (score(game, "X") - score(game, "O")), move


# computer maximizes
def Max(game, a, b, iteration):
    iteration = iteration - 1
    moves = possibleMoves(game, "X")
    move = -100
    value = -10000
    if(iteration != 0):
        for item in moves:
            if(game != None):
                game = MakeMove(game, item, "X")
                nextValue, next = Min(game, a, b, iteration)
                if (value < nextValue):
                    value = nextValue
                    move = item
                    b = max(b, value)
                if (value <= a):
                    return value, move
    return (score(game, "X") - score(game, "O")), move


# agent will be maximizing player in the minimax algorithm
def Agent(game):
    temp = copy.deepcopy(game)
    value, move = Max(temp, 10000, -10000, 30)
    if(move != -100):
        game = MakeMove(temp, move, "X")
    else:
        print("the AI has run out of moves, or was unable to make a decision")
        exit(404)
    return game


Start(GameState)
