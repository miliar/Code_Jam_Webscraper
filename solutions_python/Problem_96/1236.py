#Dylan Nelson
#Problem B
IFILE = 'B-large.in'
OFILE = 'B-large.out'
#=============================================================================

def maxD(totals, surp, p):
    o = 0
    for t in totals:
        if t in (29, 30):
            if 10 >= p : o += 1
        elif t == 1:
            if 1 >= p : o += 1
        elif t == 0:
            if 0 >= p : o += 1
        else:
            b = breakUp(t)
            if b[1] >= p: o += 1
            else:
                if (b[0] >= p) and (surp > 0):
                    o += 1
                    surp -= 1
    return str(o)

def breakUp(score):
    if (score % 3) == 0:
        return [score // 3 + 1, score //3]
    elif (score % 3) == 1:
        return [score // 3 + 1, score // 3 + 1]
    else:
        return [score // 3 + 2, score // 3 + 1]

#=============================================================================
fin = open(IFILE, 'r')
fout = open(OFILE, 'w')
T = int(fin.readline())
for i in range(1, T + 1):
    line = [int(i) for i in fin.readline().split()]
    fout.write('Case #' + str(i) + ': ' + maxD(line[3:], line[1], line[2]) + '\n')
fin.close()
fout.close()
