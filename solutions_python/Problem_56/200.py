#!/usr/bin/env python

def check(arr, K, BR):
    for item in arr:
        if len(item) < K: continue
        if BR * K in item:
            return True
    return False

def build(inarr, order):
    arr = []
    N = len(inarr)
    if order == 1: #horizontal
        for inlst in inarr:
            arr.append(''.join(inlst))
    elif order == 2: #vertical
        for i in range(N):
            s = ''
            for j in range(N):
                s += inarr[j][i]
            arr.append(s)
    elif order == 3: # left-top ->
        for i in range(N):
            s = ''
            for j in range(N - i):
                s += inarr[j][i+j]
            arr.append(s)
    elif order == 4: # left-bottom ->
        for i in range(N):
            s = ''
            for j in range(N - i):
                s += inarr[N - j - 1][i+j]
            arr.append(s)
    return arr


#infile = "A-large.in"
infile = "A-small-attempt1.in"
#infile = "A-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    N, K = [int(value) for value in fsrc.readline().split()]
    one_line = ['.' for i in range(N)]
    arr = [ one_line[:] for i in range(N)]
    
    print K
    #read array
    for i in range(N):
        src_arr = list(fsrc.readline().strip().replace('.', ''))
        src_arr.reverse()
        j = 1
        for elem in src_arr[:]:
            arr[i][N-j] = elem
            j += 1
        print arr[i]

    #solve
    blue = False
    red = False
    for i in range(4):
        lst = build(arr, i+1)
        print lst
        if not blue: blue = check(lst, K, 'B')
        if not red: red = check(lst, K, 'R')
        if blue and red: break

    
    res = "Case #%s: " %(t+1, )
    if blue and red: res += 'Both'
    elif blue: res += 'Blue'
    elif red: res += 'Red'
    else: res += 'Neither'
    
    
    res += '\n'
    print res,
    fres.write(res)

fsrc.close()
fres.close()
