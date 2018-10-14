#!/usr/bin/env python
import fractions 

def gcd(a,b):
    return fractions.gcd(a,b)

def scm(a,b):
    return a*b/gcd(a,b)
           
def common(a,b):
    g = gcd(a,b)
    return g, a*b/g

def m(a,b):
    if a >= b:
        g = a
        s = b
    else:
        g = b
        s = a
    if g % s == 0:
        return g,s
    else:
        return False

def adjust(new,result):
    if new == 1:
        return result
    if len(result) == 0:
        return [new]
    if new in result:
        return result
    if new % result[-1] == 0:
        return result + [new]
    if result[-1] % new == 0:
        return adjust(new,result[:-1]) + [result[-1]]
    s = scm(result[-1],new)
    g = gcd(result[-1],new)
    if g == 1:
        return [s]
    return [g,s]

def solve(list):
    if len(list) == 1:
        return list
    else:
        last = solve(list[1:])
        result = adjust(list[0],last)
        return result

def find(L,H,list):
    if len(list) == 1:
        result = L/list[0] * list[0]
        tr = result
        if tr < L:
            tr += list[0]
        if tr> H:
            return None
        else:
            return tr

    if len(list) >= 2:
        if list[0] < L:
            pass
        else:
            for i in range(L,H+1):
                if list[0] % i == 0:
                    return i
        return find(L,H,list[1:])


def ffind(L,H,list):
 
    for i in range(L,H+1):
        get = True
        for l in list:
            if (l >= i and l % i == 0) or (l<i and i %l == 0):
                continue
            else:
                get = False
        if get == True:
            return i
    return False
        

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for case in range(a):
        N,L,H = map (int,f.readline().split())
        list = map (int,f.readline().split())

        result = ffind(L,H,list)   


        if result == False:
            print "Case #"+str(case+1)+": NO"
        else:
            print "Case #"+str(case+1)+":", result
