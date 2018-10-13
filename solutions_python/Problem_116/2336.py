def compare(s, flag):

    if (s == 'XXXX'):
        flag = 1
    elif (s == 'OOOO'):
        flag = 0
    elif (s.find('T') != -1):
        c = 0
        for l in s:
            if 'X' == l:
                c = c + 1
            if 'O' == l:
                c = c - 1
        if (c == 3):
            flag = 1
        elif (c == -3):
            flag = 0
        else:
            flag = 2
    else:
        flag = 2
    return flag

def validate(m):

    flag = 0
    for i in xrange(4):
        flag = compare(m[i], flag)
        if flag != 2:
            break

    if (flag == 2):
        temp1 = ""
        temp2 = ""
        for i in xrange(4):
            for j in xrange(4):
                if (i==j):
                    temp1 += m[i][j]
                if (i+j == 3):
                    temp2 += m[i][j]
        flag = compare(temp1, flag)
        if (flag == 2):
            flag = compare(temp2, flag)

    if (flag == 2):
        for i in xrange(5):
            t1 = ""
            for j in xrange(4):
                if i < 4:
                    t1 += m[j][i]
                else:
                    t1 = ""
            if t1 != "":
                if (flag == 2):
                    flag = compare(t1, flag)

    if (flag != 0 and flag != 1):
        for s in m:
            if (s.find('.') != -1):
                flag = 3
                break
    return flag

def evalfile():

    f = open('A-large.in', 'r+')
    f.seek(0)
    f2 = open('Out.txt','w')
    f2.seek(0)
    matrix = [0,0,0,0]
    t = 0
    for num, line in enumerate(f, start = 0):
        n = num % 5
        if num == 0:
            test = int(line)
        else:
            if n == 0:
                t = t + 1
                flag = validate(matrix)
                matrix = [0,0,0,0]
                if flag == 0:
                    f2.write("Case #%d:"%t + " " + "O won\n")
                elif flag == 1:
                    f2.write("Case #%d:"%t + " " + "X won\n")
                elif flag == 3:
                    f2.write("Case #%d:"%t + " " + "Game has not completed\n")
                else:
                    f2.write("Case #%d:"%t + " " + "Draw\n")
            matrix[n-1] = line.strip("\n")
    '''
    flag = validate(matrix)
    if flag == 0:
        f2.write("Case #%d:"%t + " " + "O won")
    elif flag == 1:
        f2.write("Case #%d:"%t + " " + "X won")
    elif flag == 3:
        f2.write("Case #%d:"%t + " " + "Game not completed")
    else:
        f2.write("Case #%d:"%t + " " + "Draw")
    '''

if __name__ == "__main__":

    evalfile()
