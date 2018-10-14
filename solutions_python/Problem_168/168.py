ouf = open('output.txt', 'w')
t = int(input())

def ifr(i, j):
    global c
    while j <= c - 2:
        j += 1
        if mat[i][j] != '.':
            return True
    return False

def ifl(i, j):
    global c
    while j >= 1:
        j -= 1
        if mat[i][j] != '.':
            return True
    return False

def ifd(i, j):
    global r
    while i <= r - 2:
        i += 1
        if mat[i][j] != '.':
            return True
    return False

def ifup(i, j):
    global r
    while i >= 1:
        i -= 1
        if mat[i][j] != '.':
            return True
    return False


for test in range(1, t + 1):
    r, c = map(int, input().split())
    mat = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        line = input().rstrip()
        for j in range(len(line)):
            mat[i][j] = line[j]
    flag1 = True
    cnt = 0
    for i in range(r):
        for j in range(c):
            flag = False
            if mat[i][j] == 'v':
                if ifd(i, j):
                    flag = True
                else:
                    if ifl(i, j) or ifr(i, j) or ifup(i, j):
                        cnt += 1
                    else:
                        flag1 = False
            if mat[i][j] == '^':
                if ifup(i, j):
                    flag = True
                else:
                    if ifl(i, j) or ifr(i, j) or ifd(i, j):
                        cnt += 1
                    else:
                        flag1 = False
            if mat[i][j] == '>':
                if ifr(i, j):
                    flag = True
                else:
                    if ifl(i, j) or ifup(i, j) or ifd(i, j):
                        cnt += 1
                    else:
                        flag1 = False
            if mat[i][j] == '<':
                if ifl(i, j):
                    flag = True
                else:
                    if ifup(i, j) or ifr(i, j) or ifd(i, j):
                        cnt += 1
                    else:
                        flag1 = False
    if flag1 == False:
        print('Case #', test, ': ', 'IMPOSSIBLE', sep = '', file = ouf)
    else:
        print('Case #', test, ': ', cnt, sep = '', file = ouf)


ouf.close()