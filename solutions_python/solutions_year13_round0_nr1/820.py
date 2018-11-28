
import sys



def mul(x, y):
    return x * y

def sumprod(x, y):
    return sum(map(mul, x, y))

def checkArray(arr):
    print arr
    if '.' in arr:
        return '.'
    elif ('T' in arr and arr.count('X') == 3) or arr.count('X') == 4:
        return 'X'
    elif ('T' in arr and arr.count('O') == 3) or arr.count('O') == 4:
        return 'O'


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        matrix = list()
        strings = list()
        for i in range(4):
            matrix.append(inputfile.readline().rstrip('\r\n'))
            strings.append(matrix[i])
        inputfile.readline() # throw away space

        #Create 10 strings to test:
        strings.append(matrix[0][0] + matrix[1][0] + matrix[2][0] + matrix[3][0])
        strings.append(matrix[0][1] + matrix[1][1] + matrix[2][1] + matrix[3][1])
        strings.append(matrix[0][2] + matrix[1][2] + matrix[2][2] + matrix[3][2])
        strings.append(matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][3])
        strings.append(matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3])
        strings.append(matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0])


        results = list()
        for line in strings:
            results.append(checkArray(line))

        print results
        result = 'Draw'
        if 'X' in results:
            result = 'X won'
        elif 'O' in results:
            result = 'O won'
        elif '.' in results:
            result = 'Game has not completed'


        # check rows
        # check columns
        # check diagonals
        # check



        outputline = "Case #" + str(m + 1) + ": " + result + "\n"
        print outputline
        outputfile.write(outputline)

