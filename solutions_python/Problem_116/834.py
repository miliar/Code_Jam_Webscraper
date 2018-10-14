def check(b):
    line = genlist(b)
    for i in line:
        for j in i:
            if j != 'O' and j != 'T':
                break
        else:
            return 'O won'

        for j in i:
            if j != 'X' and j != 'T':
                break
        else:
            return 'X won'

    for i in b:
        for j in i:
            if j == '.':
                return 'Game has not completed'
    return 'Draw'

def genlist(b):
    l = []
    for i in b:
        l.append(i)
    for i in range(4):
        l.append(b[0][i]+b[1][i]+b[2][i]+b[3][i])
    l.append(b[0][0]+b[1][1]+b[2][2]+b[3][3])
    l.append(b[0][3]+b[1][2]+b[2][1]+b[3][0])
    return l

def readboard():
    b = []
    for i in range(4):
        b.append(raw_input())
    raw_input()
    return b

def main():
    count = int(raw_input())
    for i in range(count):
        b = readboard()
        print "Case #"+str(i+1) + ": ", check(b)

main()
