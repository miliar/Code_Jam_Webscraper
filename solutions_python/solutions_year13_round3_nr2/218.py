from math import sqrt, pow, log, ceil, log10
from sys import stdin, stderr
import random
import collections

# Useful for reduce
def mul(x,y):
    return x * y

def add(x,y):
    return x + y

def max(x, y):
    if x > y:
        return x
    return y

def min(x, y):
    if x < y:
        return x
    return y

def jump(x,y,n,d):
    if d == 'N':
        return (x,y+n)
    elif d == 'S':
        return (x,y-n)
    elif d == 'E':
        return (x+n,y)
    elif d == 'W':
        return (x-n,y)

def where(x,y):
    where = [(0,0,'')]
    already = [(0,0)]

    for i in range(1,30+1):
        print where
        print len(where), len(already), i

        for w in where[:]:
            x1,y1,s1 = w
            xn,yn = jump(x1,y1,i,'N')
            xs,ys = jump(x1,y1,i,'S')
            xe,ye = jump(x1,y1,i,'E')
            xw,yw = jump(x1,y1,i,'W')

            if (xs,ys) not in already:
                where.append((xs,ys,s1+'S'))
                already.append((xs,ys))
            if (xn,yn) not in already:  
                where.append((xn,yn,s1+'N'))
                already.append((xn,yn))
            if (xe,ye) not in already:
                where.append((xe,ye,s1+'E'))
                already.append((xe,ye))
            if (xw,yw) not in already:
                where.append((xw,yw,s1+'W'))
                already.append((xw,yw))

            if (xn,yn) == (x,y):
                return s1+'N'
            if (xs,ys) == (x,y):
                return s1+'S'
            if (xe,ye) == (x,y):
                return s1+'E'
            if (xw,yw) == (x,y):
                return s1+'W'

        # l = [(x1,y1,s1) for (x1,y1,s1) in nwhere if x1 == x and y1 == y]

        # if len(l) > 0:
        # #    print l
        #     return l[0][2]

        # for w1 in where[:]:
        #     x1,y1,s1 = w1
        #     for w2 in where[:]:
        #         x2,y2,s2 = w2
        #         if x1 == x2 and y1 == y2 and (s1 != s2) and (len(s2) > len(s1)):
        #             if w2 in where:
        #                 where.remove(w2)

    return None

def go(x,y,r, rmin):
    x0 = 0
    y0 = 0
    s = ''

    for i in range(r, rmin-1, -1):
        if abs(x-x0) > abs(y-y0):
            if x0 < x:
                x0 += i + 1
                s = 'E' + s
            else:
                x0 -= i + 1
                s = 'W' + s
        else:
            if y0 < y:
                y0 += i + 1
                s = 'N' + s
            else:
                y0 -= i + 1
                s = 'S' + s

    return (x0,y0,s)

def comp(s):
    x = y = 0
    i = 0
    for c in s:
        i += 1
        if c == 'N':
            y += i
        if c == 'S':
            y -= i
        if c == 'E':
            x += i
        if c == 'W':
            x -= i
    return (x,y)

# Main part
T = int(stdin.readline())

for i in range(1,T+1):

    print "Case #" + str(i) + ":",

    x, y = map(int, stdin.readline().split())
    # print where(x,y)

    for j in range(1,100):
        g = go(x,y,j,0)
        (x0,y0,s0) = g
        if (x0,y0) == (x,y):
            if comp(s0) == (x,y):
                print s0
            else:
                print "Error", s0, comp(s0), (x,y)
            break



