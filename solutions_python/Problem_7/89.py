def main(cords):
    ret = 0
    for x in range(len(cords)):
        for y in range(x+1, len(cords)):
            for z in range(y+1, len(cords)):
                if (cords[x][0]+cords[y][0]+cords[z][0])%3 == 0 and \
                    (cords[x][1]+cords[y][1]+cords[z][1])%3 == 0:
                        ret = ret + 1

    return ret

f = open('A-small-attempt0.in','r')
c = 1

for y in range(int(f.readline())):
    cords = []
    l = f.readline().strip().split(' ')
    n = int(l[0])
    A = int(l[1])
    B = int(l[2])
    C = int(l[3])
    D = int(l[4])
    x = int(l[5])
    y = int(l[6])
    M = int(l[7])
	
    cords.append((x, y))
    for z in range(n-1):
        x = (A*x+B) % M
        y = (C*y+D) % M
        cords.append((x, y))

    print 'Case #'+str(c)+':',main(cords)
    c = c + 1
