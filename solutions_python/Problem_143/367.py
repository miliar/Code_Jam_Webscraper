from itertools import groupby

f = open('input.in')
g = open('output', 'w')

T = int(f.readline()[:-1])

for case in range(T) :
    A, B, K = map(int, f.readline()[:-1].split())
    # print A, B, K
    c = 0
    for a in range(A) :
        for b in range(B) :
            if a & b < K : c += 1
    # print c
    res = c
    output = 'Case #' + str(case+1) + ': ' + str(res)
    g.write(output + '\n')
    print output

f.close()
g.close()
