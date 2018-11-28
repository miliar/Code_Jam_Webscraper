



T = int(raw_input())
case_number = 1
while case_number <= T:
    line = raw_input().split()
    p = [(1 if c == '+' else 0) for c in line[0]]
    k = int(line[1])
    n = 'IMPOSSIBLE'
    if all(c==1 for c in p):
        n = 0
    else:
        t = 0
        for i in range(0, len(p)-k+1):
            # print p, i
            if p[i] == 0:
                for d in range(k):
                    p[i + d] = 1 - p[i + d]
                t += 1
        if all(c==1 for c in p):
            n = t

    print 'Case #{0}: {1}'.format(case_number, n)
    case_number += 1

