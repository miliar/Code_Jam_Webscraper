#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def check (arr):
    #print arr
    nO = arr.count('O')
    nX = arr.count('X')
    nT = arr.count('T')
    if nO + nT == 4:
        return 'O won'
    if nX + nT == 4:
        return 'X won'
    return None

def main():
    pass

if __name__ == '__main__':
    main()

result = []
N = 0

with open('A-large.IN') as f:
    N = int(f.readline())

    for i in range(0, N):
        str = ''
        for j in range( 0, 4):
            str = str + f.readline().strip()
        ##
        rs = None
        for k in range(0, 4):
            #row
            if rs == None:
                rs = check( (str[k*4], str[k*4 + 1], str[k*4 + 2], str[k*4 + 3] ) )
            if rs == None:
                rs = check( (str[k], str[4 + k], str[8 + k], str[12 + k] ) )

        if rs == None:
            rs = check ( (str[0], str[4 + 1], str[8 + 2], str[ 12 + 3]) )

        if rs == None:
            rs = check ( (str[3], str[4 + 2], str[8 + 1], str[ 12 + 0]) )

        if rs != None:
            result.append(rs)
        else:
            if str.find('.') > -1:
                result.append('Game has not completed')
            else:
                result.append('Draw')
        ##
        f.readline()
    ########################33

with open('A-large.OUT', 'w') as f:
    for  i in range(0, N):
        f.write("Case #%d: %s\n" % (i+1, result[i]) )
