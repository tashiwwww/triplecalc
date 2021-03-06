pieces = [1,2,3,4,5,6,7]
width = 7
height = 7
piecenames = ['grass','bush','tree','hut','house','mansion','castle']

def getinput():
    'Get user input and do stuff'
    key = input("Enter a number or 'H' for help: ")
    if key == 'L' or key == 'l':
        legend()
        getinput()
    if key == 'H' or key == 'h':
        help()
        getinput()
    if key == 'S' or key == 's':
        showboard(board)
        getinput()
    if key == 'Q' or key == 'q':
        print("gg")
        return
    else:
        try:
            if int(key) in pieces:
                print("You chose: " + piecenames[int(key)-1])
                loc = input("Input coordinates: ")
                if loc == 'Q' or loc == 'q':
                    print("gg")
                    return
                pos = posparse(loc)
                if pos != False:
                    if placepiece(int(key),pos):
                        checkpieces(pos)
                        showboard(board)
                getinput()
        except ValueError:
            print("I don't know what you're doing. Try again")
            getinput()
    return
                
def legend():
    'Print legend of structures/numbers'
    print('1 = grass')
    print('2 = bush')
    print('3 = tree')
    print('4 = hut')
    print('5 = house')
    print('6 = mansion')
    print('7 = castle')
    return

def placepiece(piece,pos):
    'update a position with a piece value'
    x = pos[0]
    y = pos[1]
    if board[y][x] > 0:
        print("There's already a piece there.")
        return False
    board[y][x] = piece
    return True

def posparse(pos):
    'parse A5 into 1, -3 or whatever'
    if len(pos) != 2:
        print("Coordinates should be 2 characters")
        return False
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    try:
        x = alphabet.index(pos[0].lower())
    except ValueError:
        print("Coordinates follow pattern 'C1' or 'A2' etc")
        return False
    return [int(x),-int(pos[1])]

def checkpieces(pos):
    'check if match 3 and convert'
    x = pos[0]
    y = pos[1]
    lastpiece = board[y][x]
    search(lastpiece,[y,x])
    return True
def search(piece,pos,skip=False,matched=1,hits=[]):
    'search adjacent squares for matching pieces'
    if pos not in hits:
        hits.append(pos)
    dirs = ['n','e','s','w']
    dirnum = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in dirs:
        if i != dirs[skip] or skip is False:
            shift = dirnum[dirs.index(i)]
            adjacent = [sum(pair) for pair in zip(pos,shift)]
            y = adjacent[0]
            x = adjacent[1]
            if y < 0 and y > -height and x >= 0 and x < width and board[y][x] == piece:
                matched += 1
                if adjacent not in hits:
                    hits.append(adjacent)
                print(i,matched,adjacent)
                search(piece,adjacent,dirs.index(i)-2,matched,hits)
    if matched >= 3:
        matched = 0
        for square in hits:
            x = square[1]
            y = square[0]
            board[y][x] = 0
        if len(hits) > 0:
            board[hits[-1][0]][hits[-1][1]] = piece+1
            if search(piece+1,[hits[-1][0],hits[-1][1]]) >= 3:
                board[hits[-1][0]][hits[-1][1]] = piece+2
        del hits[:]
    print(hits)
    return matched
def help():
    'show instructions'
    print("Input 'L' for a list of pieces.")
    print("'S' to show the board")
    print("'Q' quits")
    print("Input a number to place a piece. After that, you will be prompted for the coordinates. Starting from the bottom left corner, use letters across and numbers going up. For example, B2 is the 2nd column, second row from the bottom left.")
    return
def newboard(x = 7,y = 7):
    'clear the board and set to x and y dimensions'
    board = [0] * x
    for i in range(x):
        board[i] = [0] * y
    board[0][0] = '_'
    return board
def showboard(board):
    'show the board'
    for row in board:
        print(row)
    return

board = newboard(width,height)
showboard(board)
getinput()

