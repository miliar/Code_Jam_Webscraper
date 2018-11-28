def checkCell(x, y):
    c = True
    height = h[x][y]
    i = 0
    while i < X:
        if h[x][i] > height:
            c = False
            break
        i += 1
    if c: return True
    i = 0
    c = True
    while i < Y:
        if h[i][y] > height:
            c = False
            break
        i += 1
    if c: return True

input = open('B-small-attempt0.in','r')
n = int(input.readline())
ret = ''
t = 0
while t < n:
    [Y,X] = input.readline().split()
    X = int(X)
    Y = int(Y)

    h = []
    j = 0
    while j < Y:
        h.append(input.readline().split())
        j += 1
    
    c = True
    j = 0
    while j < Y:
        i = 0
        while i < X:
            if not checkCell(j,i):
                c = False
                break
            i += 1
        if not c: break
        j += 1
    ret+= 'Case #'+str(t+1)+': '
    if c: ret+= 'YES\n'
    else: ret+= 'NO\n'
    t += 1

output = open('output.txt', 'w')
output.write(ret)
output.close()
