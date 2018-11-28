from multiprocessing import Process, Queue
import sys

def getnext(N):
    n = [int(i) for i in N]
    data = []
    for i in range(len(n)-1, -1, -1):
        for j in range(i, -1, -1):
            if n[j] < n[i]:
                data.append((j,i))
                
    if len(data) > 0:
        i = -1
        j = -1
        for p,q in data:
            if j < p:
                j = p
                i = q
        t = n[j]
        n[j] = n[i]
        n[i] = t
        sub = n[j+1:]
        sub.sort()
        t = n[:j+1]
        t.extend(sub)
        n = t
    else:
        n.append(0)
        n.sort()
        v = 0
        for v in n:
            if v != 0:
                break
        n.remove(v)
        n.insert(0, v)
    return int(''.join([str(c) for c in n]))

f = open(sys.argv[1])
T = int(f.readline())
for tc in range(1, T+1):
    N = f.readline().strip()
    n = getnext(N)
    print("Case #%d: %d" % (tc, n))
    if n <= int(N):
        break
    
        
