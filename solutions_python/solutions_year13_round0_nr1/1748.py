f = open('A-small-attempt0.in')
#f = open('test.in')
count = int(f.readline())
output = ''
matrix = [[]] * 4
hasEmptyCell = False
winner = 0

def rowCheck():
    return check(matrix[0]) | check(matrix[1]) | check(matrix[2]) | check(matrix[3])

def columnCheck():
    return check([matrix[0][0],matrix[1][0],matrix[2][0],matrix[3][0]]) | check([matrix[0][1],matrix[1][1],matrix[2][1],matrix[3][1]]) | check([matrix[0][2],matrix[1][2],matrix[2][2],matrix[3][2]]) | check([matrix[0][3],matrix[1][3],matrix[2][3],matrix[3][3]])

def crossCheck():
    return check([matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]]) | check([matrix[0][3],matrix[1][2],matrix[2][1],matrix[3][0]])

def check(arr):
    global hasEmptyCell,winner
    temp = 0
    for i in range(0,4):
        if arr[i] == '.':
            hasEmptyCell = True
            return False
        elif arr[i] == 'T':
            continue
        else:
            if (i == 0) | (temp == 0):
                temp = arr[i]
            elif temp != arr[i]:
                return False
    winner = temp
    return True


for i in range(0,count):
    matrix[0] = f.readline()
    matrix[1] = f.readline()
    matrix[2] = f.readline()
    matrix[3] = f.readline()
    f.readline()
    hasEmptyCell = False
    winner = 0
    if rowCheck() | columnCheck() | crossCheck():
        print('winner is:'+str(winner))
        output += 'Case #' + str(i+1) + ': ' + winner + ' won\n'
    elif hasEmptyCell:
        output += 'Case #' + str(i+1) + ': Game has not completed\n'
    else:
        output += 'Case #' + str(i+1) + ': Draw\n'



print(output)
newf = open('output.txt','w')
newf.write(output)
#Case #1: X won
#Case #2: Draw
#Case #3: Game has not completed
#Case #4: O won
#Case #5: O won
#Case #6: O won
