#Dylan Nelson
#Problem C
IFILE = 'C-small-attempt0.in'
OFILE = 'C-small-attempt0.out'
#=============================================================================

def rec(A, B):
    digits = len(str(A))
    proc = set([])
    recd = []
    for i in range(A, B + 1):
        if not (i in proc):
            l = set([])
            n = str(i)
            for j in range(digits):
                n = n[1:] + n[0]
                if (A <= int(n)) and (int(n) <= B):
                    l.add(n)
                    proc.add(int(n))
            recd.append(len(l))
    tot = 0
    for i in recd:
        tot += i*(i - 1) // 2
    return str(tot)
#=============================================================================
fin = open(IFILE, 'r')
fout = open(OFILE, 'w')
T = int(fin.readline())
for i in range(1, T + 1):
    line = [int(i) for i in fin.readline().split()]
    fout.write('Case #' + str(i) + ': ' + rec(line[0], line[1]) + '\n')
fin.close()
fout.close()
