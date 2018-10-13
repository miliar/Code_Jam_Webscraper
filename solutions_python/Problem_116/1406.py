import math, sys

fin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

T = int(fin.readline())
for t in range(1, T+1):
    x_r = [True] * 4
    x_c = [True] * 4
    o_r = [True] * 4
    o_c = [True] * 4
    aa, bb, cc, dd = (True, True, True, True)
    result = 'Draw'
    isFull = True

    for r in range(4):
        line = fin.readline()[:-1]
        for c in range(4):
            if line[c] == 'X':
                o_r[r] = o_c[c] = False
                if r == c:
                    aa = False
                if r + c == 3:
                    bb = False
            elif line[c] == 'O':
                x_r[r] = x_c[c] = False
                if r == c:
                    cc = False
                if r + c == 3:
                    dd = False
            elif line[c] == '.':
                isFull = False
                o_r[r] = o_c[c] = x_r[r] = x_c[c] = False
                if r == c:
                    aa = False
                    cc = False
                if r + c == 3:
                    bb = False
                    dd = False

    for i in range(4):
        if o_r[i] or o_c[i] or aa or bb:
            result = 'O won'
            #print(str(i) + ' ' + str(aa) + str(bb))
            break
        elif x_r[i] or x_c[i] or cc or dd:
            #print(str(i) + ' ' + str(cc) + str(dd))
            result = 'X won'
            break

        
    if result == 'Draw' and isFull == False:
        result = 'Game has not completed'
    
    print('Case #' + str(t) + ': ' + result)
    fin.readline()
fin.close()
temp = sys.stdout
temp.close()
