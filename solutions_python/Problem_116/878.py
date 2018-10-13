
from sys import argv

#f = open(sys.argv[1])
f = open("A-large.in")
cases = int(f.readline())
array = [0,0,0,0]
diag = [0,0,0,0]
def checkOneLine(in_Data):
    count_X = in_Data.count('X')
    count_O = in_Data.count('O')
    count_T = in_Data.count('T')
    if count_X == 4 :
        print "Case #%d: X won"%(i+1)
        return True
    if count_O == 4 :
        print "Case #%d: O won"%(i+1)
        return True
    elif count_X == 3 and count_T == 1:
        print "Case #%d: X won"%(i+1)
        return True
    elif count_O == 3 and count_T == 1:
        print "Case #%d: O won"%(i+1)
        return True
    else:
        return False

def checkAllLine(in_array):
    for i in range(4):
        if checkOneLine(in_array[i]):
            return True
    return False

def checkEmpty(in_array):
    for j in range(4):
        if array[j].count('.'):
            print "Case #%d: Game has not completed"%(i+1)
            return True
    return False

if __name__ == "__main__":

    for i in range(cases):
        for j in range(4):
            array[j] = f.readline().strip()
        f.readline() # an empty line

        if checkAllLine(array):
            continue

        array = zip(*array)
        if checkAllLine(array):
            continue

        diag = [array[0][0], array[1][1], array[2][2], array[3][3]]
        if checkOneLine(diag):
            continue
        
        diag = [array[0][3], array[1][2], array[2][1], array[3][0]]
        if checkOneLine(diag):
            continue

        if checkEmpty(array):
            continue
        else:
            print "Case #%d: Draw"%(i+1)


    
