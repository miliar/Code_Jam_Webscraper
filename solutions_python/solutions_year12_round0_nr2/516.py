def poss(s, p, scores):
    surp  = 0
    count = 0
    for score in scores:
        f = p + (2*(p-2))
        if f < 0:
            f = 0
        if score < f or score < p:
            continue
        f = p + (2*(p-1))
        if score >= f:
            count += 1
            continue
        surp += 1
    count += min(s,surp)
    return count
        

fin = open('C:\\temp\\B-large.in')
fout = open('C:\\temp\\B-large.out','w')
cases = int(fin.readline())
for case in range(cases):
    line = fin.readline().strip('"\n')
    n = line.split(' ')
    g = int(n[0])
    s = int(n[1])
    p = int(n[2])
    scores = []
    for i in range(g):
        scores.append(int(n[i+3]))
    fout.write('Case #' + str(case+1) + ': ' + str(poss(s, p, scores)) + '\n')