#!/usr/bin/python

def solve():
    b = []
    o = []
    
    l = raw_input().split(' ')
    n = int(l.pop(0))
    for i in range(n):
        if l.pop(0) == 'O':
            o.append((i, int(l.pop(0))))
        else:
            b.append((i, int(l.pop(0))))
    
    result = 0
    pos_o = 1
    pos_b = 1
    act = 0
    advance = False
    while b or o:
        result += 1
        if b:
            if b[0][1] > pos_b:
                pos_b += 1
            elif b[0][1] < pos_b:
                pos_b -= 1
            elif b[0][0] == act:
                b.pop(0)
                advance = True
        if o:
            if o[0][1] > pos_o:
                pos_o += 1
            elif o[0][1] < pos_o:
                pos_o -= 1
            elif o[0][0] == act:
                o.pop(0)
                advance = True
        if advance:
            advance = False
            act += 1
    
    return result

if __name__ == '__main__':
    T = int(raw_input())
    for c in range(1, T+1):
        print "Case #{0}: {1}".format(c, solve())
