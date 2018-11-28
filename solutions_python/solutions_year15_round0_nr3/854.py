mat = {1:[1,2,3,4],
        2:[2,-1,4,-3],
        3:[3,-4,-1,2],
        4:[4,3,-2,-1]}

def multiply(x,y):
    if y == '1': y = 1;
    if y == 'i': y = 2;
    if y == 'j': y = 3;
    if y == 'k': y = 4;
    return mat[x][y-1]

sign = lambda x: (1, -1)[x<0]

T = int(raw_input())

for t in range(T):
    X,L=map(int,raw_input().split(' '))
    s = raw_input()
    S = s*L
    i,j,k = False,False,False
    current = 1
    for c in S:
        temp = sign(current)*multiply(abs(current),c)
        current = temp
        if i == False:
            if current == 2:
                i = True
                current = 1
                continue
            continue
        if j == False:
            if current == 3:
                j = True
                current = 1
                continue
            continue
    if current == 4:
        k = True
    result = i and j and k
    print "Case #%d: %s"%(t+1,"YES" if result else "NO")
