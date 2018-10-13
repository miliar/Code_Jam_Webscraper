n = int(input())
for x in range(n):

    D , N  = map(int , input().split())

    e = [map(int, input().split()) for x in range(N)]

    q = [(D-a)/b for a, b in e]

    mx = max(q)

    print('Case #{0}: {1:.6f}'.format(x+1, D/mx)) 

