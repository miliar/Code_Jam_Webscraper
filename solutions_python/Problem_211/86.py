in_file = 'C-small-1-attempt1.in'
out_file = 'C-small-1.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    n, k = list(map(int, inp.readline().split()))
    u = float(inp.readline())
    p = list(map(float, inp.readline().split()))
    p.sort()
    q = 1

    avg = (sum(p) + u)/n

    cont = True
    while cont:
        for i in range(len(p)):

            cont = False
            if p[i] > avg + 0.00000001:
                for j in range(i, len(p)):
                    q *= p[j]
                p = p[:i]
                cont = True
                avg = (sum(p) + u)/len(p)
                break

    q *= avg**len(p)

    out.write('Case #{}: {}\n'.format(case, q))

inp.close()
out.close()
