# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Qualification Round
"""

import sys

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


def once():
    '''to cope once
    return the answer to be printed'''
    s, k = IO.gets()
    k = int(k)
    s = [c == '+' for c in s]
    cnt = 0
    for i in range(len(s) - k + 1) :
        if not s[i] :
#            print(i)
            cnt += 1
            for j in range(i, i+k) :
                s[j] = not s[j]
#            print(''.join('+' if x else '-' for x in s))
    return cnt if all(s) else 'IMPOSSIBLE'

def show(ans) :
    return ans #IO.tostr(ans, writer=str, delim=' ')
    
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
