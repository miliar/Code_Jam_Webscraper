from collections import deque

T = int(raw_input())

def bfs (l):
    q = deque([(0, tuple(l))])
    visited = set()
    
    while q:
        #print q
        d, cur = q.popleft()
        l = list(cur)

        for i, x in enumerate(l):
            if i < x:
                break
        else:
            return d

        for i in range(len(l)-1):
            j = i+1
            l[i], l[j] = l[j], l[i]
            t = tuple(l)
            if t not in visited:
                visited.add(t)
                q.append((d+1, t))
            l[i], l[j] = l[j], l[i]

def rindex(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] == '1':
            return i
    else:
        return -1

for case in xrange(1, T+1):
    n = int(raw_input())
    matrix = [rindex(raw_input()) for i in range(n)]
    print 'Case #%i: %i' % (case, bfs(matrix))
