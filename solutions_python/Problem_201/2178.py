import math
T = int(input())

def split(s):
    if s%2==0: return (s//2-1, s//2)
    return ((s-1)//2, (s-1)//2)

def getValue(k, N):
    if k==1: return N
    pk = k//2
    p = getValue(pk, N)
    print(pk, p)
    return parentToChild(p, k)

def parentToChild(p, i):
    if p==1: return 0
    if p%2: return (p-1)//2
    if i%2: return p//2
    return p//2 - 1

with open('C.out', 'w') as fout:
    for t in range(T):
        N, K = list(map(int, input().split()))
        print(N,K)
        hlen = 2**(math.floor(math.log(K,2))+1)-1
        print(hlen)
        heap = [0 for i in range(hlen)]
        heap[0] = N
        for i in range(1,hlen):
            heap[i] = parentToChild(heap[(i-1)//2], i-1)
        hLvl = list(reversed(sorted(heap[hlen//2:])))
        v = hLvl[K-hlen//2-1]
        if v%2: y,z = (v-1)//2, (v-1)//2
        else: y, z = v//2, v//2-1
        print(y,z)
        print()
        fout.write('Case #%d: %d %d\n'%(t+1,y,z))
