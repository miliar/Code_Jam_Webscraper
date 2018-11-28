#!/usr/bin/python


def flow(i, j):
    res = min(a[i-1][j], a[i+1][j], a[i][j-1], a[i][j+1], a[i][j])
    if res == a[i][j]:
        pass
    elif res == a[i-1][j]:
        r[i][j] = '1'
    elif res == a[i][j-1]:
        r[i][j] = '2'
    elif res == a[i][j+1]:
        r[i][j] = '3'
    elif res == a[i+1][j]:
        r[i][j] = '4'

def get_res(i, j):
    
    if res[i-1][j] == '' and r[i-1][j] == '4':
        res[i-1][j] = res[i][j]
        get_res(i-1, j)
    if res[i][j-1] == '' and r[i][j-1] == '3':
        res[i][j-1] = res[i][j]
        get_res(i, j-1)
    if res[i][j+1] == '' and r[i][j+1] == '2':
        res[i][j+1] = res[i][j]
        get_res(i, j+1)
    if res[i+1][j] == '' and r[i+1][j] == '1':
        res[i+1][j] = res[i][j]
        get_res(i+1, j)
    if r[i][j] != '':
        if r[i][j] == '1' and res[i-1][j] == '':
            res[i-1][j] = res[i][j]
            get_res(i-1, j)
        elif r[i][j] == '2' and res[i][j-1] == '':
            res[i][j-1] = res[i][j]
            get_res(i, j-1)
        elif r[i][j] == '3' and res[i][j+1] == '':
            res[i][j+1] = res[i][j]
            get_res(i, j+1)
        elif r[i][j] == '4' and res[i+1][j] == '':
            res[i+1][j] = res[i][j]
            get_res(i+1, j)
        
t = raw_input()

for i in range(0, int(t)):
    string = raw_input()
    input = string.split(" ")
    a = [[100000 for row2 in range(int(input[1])+2)] for row in range(int(input[0])+2)]
    r = [['' for row2 in range(int(input[1])+2)] for row in range(int(input[0])+2)]
    for j in range(1, int(input[0])+1):
        arr = raw_input()
        array = arr.split(" ")
        for k in range(1, int(input[1])+1):
            a[j][k] = int(array[k-1])
    word = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    w = 0
    for j in range(1, int(input[0])+1):
        for k in range(1, int(input[1])+1):
            flow(j, k)
    res = [['' for row2 in range(int(input[1])+2)] for row in range(int(input[0])+2)]
    for j in range(1, int(input[0])+1):
        for k in range(1, int(input[1])+1):
            if res[j][k] == '':
                res[j][k] = word[w]
                get_res(j, k)
                w = w+1
    print 'Case #'+str(i+1)+':'
    for j in range(1, int(input[0])+1):
        o = res[j][1]
        for k in range(2, int(input[1])+1):
            o += " "+res[j][k]
        print o

