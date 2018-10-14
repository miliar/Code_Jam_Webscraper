

if __name__ == '__main__':
    inp = file('B-large.in','r')
    out = file('B-large.out','w')

    n = int(inp.readline())

    i = 1

    for line in inp:
        l = map(int, line.split())
        n, s, p, t  = l[0],l[1],l[2],l[3:]

        assigned = []
        poss = []
        for j,v in enumerate(t):
            if v == 0:
                assigned.append(0)
                continue
            if v % 3 == 0:
                q = v / 3
                assigned.append(q)
                poss.append(j)
            if (v+1) % 3 == 0:
                q = (v+1)/3
                assigned.append(q)
                poss.append(j)
            if (v+2) % 3 == 0:
                assigned.append((v+2)/3)

        def cmp(x,y):
            if assigned[x] == p-1:
                return -1
            elif assigned[y] == p-1:
                return 1

            if assigned[x] == assigned[y]:
                return 0
            elif assigned[x] > assigned[y]:
                return -1
            else:
                return 1
        
        poss.sort(cmp=cmp)
        changed = 0
        for k in xrange(len(poss)):
            if changed == s:
                break
            assigned[poss[k]] += 1
            changed += 1
        
        maxs = filter(lambda x: x >= p, assigned)

        out.write('Case #%d: %d\n' % (i,len(maxs)))
        
        i += 1
