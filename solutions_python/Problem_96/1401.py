#!/usr/bin/env python


def sign(x):
    if x>0:
        return 1
    return 0

def sure(p):
    def a(x):   
        if x>3*p - 3:
            return 1
        return 0
    return a

def candi(p):
    def a(x):
        if (x == 3*p - 3) or (x == 3*p -4 ):
            return 1
        return 0
    return a

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for case in range(a):

        line = f.readline()

        numbers = map(int, line.split())

        N = numbers[0]
        S = numbers[1]
        p = numbers[2]
        scores = numbers[3:]
        
        if p==1:
            result = sum(map(sign,scores))
        elif p==0:
            result = N
        else:
            good = sum(map(sure(p),scores))
            maybe = sum(map(candi(p),scores))
            result = good + min(maybe,S)



        print "Case #"+str(case+1)+":", result
