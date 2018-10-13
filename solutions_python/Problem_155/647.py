f = open('A-large.in')
g = open('large.out', 'w')

case = 0
T = int(f.readline()[:-1])

for line in f :
    case += 1
    line = line[:-1]
    M, S = line.split()
    M = int(M)
    S = map(int, S)
    # print M, S
    c = 0
    res = 0
    for l, s in enumerate(S) :
        if c < l :
            res += l - c
            c = l
        c += s
    output = 'Case #' + str(case) + ': ' + str(res)
    print output
    g.write(output + '\n')

f.close()
g.close()
