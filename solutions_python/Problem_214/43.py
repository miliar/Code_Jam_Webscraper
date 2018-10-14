# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1B
"""

import sys
from collections import Counter
from itertools import product, chain

class IO :
    def get(reader=str) :
        return reader(input().strip())
    def gets(reader=str, delim=None) :
        return [reader(x) for x in input().strip().split(delim)]
    def tostr(raw, writer=str, delim=' ') :
        return delim.join(writer(x) for x in raw)

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    pass

r, c = 0, 0

def all_covered(a) :
    covered = [list(row) for row in a]
    for x, y in product(range(r), range(c)) :
        if a[x][y] == '-' :
            for j in range(y+1, c) :
                if a[x][j] == '#' : break
                if covered[x][j] == '.' : covered[x][j] = '*'
            for j in range(y-1, -1, -1) :
                if a[x][j] == '#' : break
                if covered[x][j] == '.' : covered[x][j] = '*'
        elif a[x][y] == '|' :
            for i in range(x+1, r) :
                if a[i][y] == '#' : break
                if covered[i][y] == '.' : covered[i][y] = '*'
            for i in range(x-1, -1, -1) :
                if a[i][y] == '#' : break
                if covered[i][y] == '.' : covered[i][y] = '*'
    return all(x != '.' for x in chain(*covered))
    
def search(ps, a) :
    a = [list(row) for row in a]
    if len(ps) == 0 :
        if all_covered(a) :
            return True, True, a
        else :
            return True, False, None
    x, y = ps[0]
    if a[x][y] in '-|' :
        cnt = 0
        for j in range(y+1, c) :
            if a[x][j] == '#' : break
            if a[x][j] in '-|' : cnt += 1
        for j in range(y-1, -1, -1) :
            if a[x][j] == '#' : break
            if a[x][j] in '-|' : cnt += 1
        if cnt == 0 :
            a[x][y] = '-'
            ans = search(ps[1:], a)
            if not ans[0] : return ans
            if ans[0] and ans[1] : return ans
        cnt = 0
        for i in range(x+1, r) :
            if a[i][y] == '#' : break
            if a[i][y] in '-|' : cnt += 1
        for i in range(x-1, -1, -1) :
            if a[i][y] == '#' : break
            if a[i][y] in '-|' : cnt += 1
        if cnt == 0 :
            a[x][y] = '|'
            ans = search(ps[1:], a)
            if not ans[0] : return ans
            if ans[0] and ans[1] : return ans
        return False, False, None
    else :
        return search(ps[1:], a)
        
def once():
    global r, c
    r, c = IO.gets(int)
    m = [list(IO.get()) for _ in range(r)]
    return search(list(product(range(r), range(c))), m)[1:]
        

def show(ans) :
    flag, a = ans
    return 'POSSIBLE' + '\n' + '\n'.join(''.join(row) for row in a) if flag else 'IMPOSSIBLE'
    
def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = IO.get(int)
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, show(ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework done with", msg, file=sys.stderr)
    main()
