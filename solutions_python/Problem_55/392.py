import sys
fin = open('C-small-attempt0.in','r')
sys.stdout = open('C-small-attempt0.out','w')
T = int(fin.readline())

def bsearch(q,value):
    l,h = [1, N]
    while l < h:
        if table[q][(l+h)//2] > value:
            h = (l+h)//2-1
        elif table[q][(l+h)//2] < value:
            l = (l+h)//2+1
        else:
            return (l+h)//2
    i = (l+h)//2
    while i > 0 and table[q][i] > value: i-=1
    return i

for cs in range(1,T+1):
    R,k,N = [int(x) for x in fin.readline().split(' ')]
    queue = [int(x) for x in fin.readline().split(' ')]
    table = [[0 for y in range(0,N+1)] for x in range(0,N)]
    for i in range(0,N):
        for j in range(0,N):
                table[i][j%N+1] = table[i][j%N]+queue[(i+j)%N]
    seat = k
    qt = 0
    ans = 0
    while R > 0:
        if table[qt][1] > seat:
            R-=1
            seat = k
        if table[qt][1] > seat:
            break
        if R > 0:
            maxjump = bsearch(qt,seat)
            R-=1
            ans += table[qt][maxjump]
            qt = (qt+maxjump)%N
    print('Case #%d: '%cs,end = '')
    print(ans)
fin.close()
