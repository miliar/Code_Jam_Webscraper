fin = open('B-large.in', 'r')
fout = open('B-output-large.txt', 'w')

cases = int(fin.readline()[:-1])

for case in range(cases) :
    line = map(int, fin.readline()[:-1].split(' '))
    N, S, p = line[:3]
    T = line[3:]
    okLimit = p + 2*max(p-1,0)
    okIfSLimit = p + 2*max(p-2,0)
    res = 0
    for t in T :
        if t >= okLimit :
            res += 1
        elif t >= okIfSLimit and S > 0 :
            res += 1
            S -= 1
    # print 'Case #' + str(case+1) + ': ' + str(res)
    fout.write('Case #' + str(case+1) + ': ' + str(res) + '\n')
    
fin.close()
fout.close()
