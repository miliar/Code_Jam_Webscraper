
from collections import deque

def get_int():
    return int(get_word())

def get_word():
    if not 'words' in dir(get_word):
        get_word.words=[]
    while len(get_word.words)==0:
        get_word.words=raw_input().split()
    return get_word.words.pop(0)

def test(k, R, g):
    e=0
    while R:
        x = k
        n = []
        while g and g[0]<=x:
            x-=g[0]
            e+=g[0]
            n.append(g.popleft())
        g.extend(n)
        R-=1
    return e

T = get_int()
for i in range(T):
    R,k,N = get_int(),get_int(),get_int()
    q = deque([get_int() for j in range(N)],N)
    print 'Case #'+str(i+1)+': '+str(test(k,R,q))
