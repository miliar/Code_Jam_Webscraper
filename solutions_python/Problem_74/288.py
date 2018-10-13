#! /usr/bin/env python

def solve() :
    ss = raw_input().split()
    ss = ss[1:]    
    
    O = []
    B = []
    side = []
    i = 0
    while i < len(ss):
        side.append(ss[i])
        if ss[i] == 'O':
            O.append(int(ss[i + 1]))
        if ss[i] == 'B':
            B.append(int(ss[i + 1]))
        i += 2

    o = 1
    b = 1
    res = 0
    while len(side) > 0:
        push = False
        if len(O) > 0:
            if O[0] == o and side[0] == 'O':
                O = O[1:]
                push = True
            elif o < O[0] : 
                o += 1
            elif o > O[0] :
                o -= 1

        if len(B) > 0:
            if B[0] == b and side[0] == 'B':
                B = B[1:]
                push = True
            elif b < B[0] : 
                b += 1
            elif b > B[0] :
                b -= 1
        res += 1
        if push:
            del side[0]
                    
    return res

def main() :
    T = int(raw_input())
    for tno in range(T):
        res = solve()
        print "Case #" + str(tno + 1)+ ": " + str(res)

if __name__ == '__main__':
    main()
