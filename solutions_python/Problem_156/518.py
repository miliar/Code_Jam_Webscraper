f = open('B-small.in')
g = open('small.out', 'w')

T = int(f.readline()[:-1])

def solve(l, c) :
    m = max(l)
    if m <= 3 : return c + m
    l1, l2 = l[:], [i - 1 for i in l if i > 1]
    if m < 9 :
        l1[l1.index(m)] = m/2
        l1.append(m - m/2)
    else :
        l1[l1.index(m)] = 6
        l1.append(3)
    return min(solve(l1, c + 1), solve(l2, c + 1), c + m)

for case in range(T) :
    D = int(f.readline()[:-1])
    D = map(int, f.readline()[:-1].split())
    res = solve(D, 0)
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print output
    g.write(output + '\n')

f.close()
g.close()
