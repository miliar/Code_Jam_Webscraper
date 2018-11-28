#!/usr/bin/python


def hcheck(M):
    for i in range(4):
        x = 0
        o = 0
        for j in range(4):
            if M[i][j] == 'X': x+=1
            if M[i][j] == 'O': o+=1
            if M[i][j] == 'T':
                x+=1
                o+=1
        if x == 4:
            return 'X'
        if o == 4:
            return 'O'

def vcheck(M):
    for j in range(4):
        x = 0
        o = 0
        for i in range(4):
            if M[i][j] == 'X': x+=1
            if M[i][j] == 'O': o+=1
            if M[i][j] == 'T':
                x+=1
                o+=1
        if x == 4:
            return 'X'
        if o == 4:
            return 'O'


def dcheck(M):
    x, o = 0, 0
    for i in range(4):
        if M[i][i] == 'X': x+=1
        if M[i][i] == 'O': o+=1
        if M[i][i] == 'T':
            x+=1
            o+=1
        if x == 4:
            return 'X'
        if o == 4:
            return 'O'
    
    x, o = 0, 0
    for i in range(4):
        
        if M[3-i][i] == 'X': x+=1
        if M[3-i][i] == 'O': o+=1
        if M[3-i][i] == 'T':
            x+=1
            o+=1
        if x == 4:
            return 'X'
        if o == 4:
            return 'O'

def isfull(M):
    return not any(('.' in s for s in M))
    
def check(M):
    h = hcheck(M)
    v = vcheck(M)
    d = dcheck(M)
    
    if h is not None:
        return h + ' won'
    if v is not None:
        return v + ' won'
    if d is not None:
        return d + ' won'
    if isfull(M):
        return 'Draw'
    return 'Game has not completed'
    
cases = int(raw_input())
for i in range(cases):
    M = list()
    if i > 0:
        raw_input()
    for j in range(4):
        M.append(raw_input())
    res = check(M)
    print "Case #%d: %s" % (i+1, res)