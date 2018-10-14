from heapq import heappush, heappop


def gen_empty_field(R, C):
    field = []
    for i in xrange(0, R):
        field.append([])
        for j in xrange(0, C):
            field[-1].append('*')
    return field


def dup_field(field):
    nfield = []
    for r in field:
        nfield.append(r[:])
    return nfield


def get_expansions(field, nspace):
    expansions = []
    R = len(field)
    C = len(field[0])
    for r in xrange(0, R):
        for c in xrange(0, C):
            if field[r][c] in ['.', 'c']:
                nfield = dup_field(field)
                nchange = 0
                if r > 0 and field[r-1][c] == '*':
                    nchange += 1
                    nfield[r-1][c] = '.'
                if c > 0 and field[r][c-1] == '*':
                    nchange += 1
                    nfield[r][c-1] = '.'
                if r < R-1 and field[r+1][c] == '*':
                    nchange += 1
                    nfield[r+1][c] = '.'
                if c < C-1 and field[r][c+1] == '*':
                    nchange += 1
                    nfield[r][c+1] = '.'
                if r > 0 and c > 0 and field[r-1][c-1] == '*':
                    nchange += 1
                    nfield[r-1][c-1] = '.'
                if r > 0 and c < C-1 and field[r-1][c+1] == '*':
                    nchange += 1
                    nfield[r-1][c+1] = '.'
                if r < R-1 and c > 0 and field[r+1][c-1] == '*':
                    nchange += 1
                    nfield[r+1][c-1] = '.'
                if r < R-1 and c < C-1 and field[r+1][c+1] == '*':
                    nchange += 1
                    nfield[r+1][c+1] = '.'

                if nchange > 0:
                    expansions.append((nspace+nchange, nfield))

    return expansions


def solve(R, C, M):

    nsize = R * C - M

    for r in xrange(0, R):
        for c in xrange(0, C):
            sheap = []
            field = gen_empty_field(R, C)
            field[r][c] = 'c'
            heappush(sheap, ((1, field)))
            top = None
            ans = None

            while len(sheap) > 0:
                #print ">>>> %s %s " % (r, c)
                top = heappop(sheap)
                #print len(sheap)

                if top[0] == nsize:
                    ans = top[1]
                    break

                elif top[0] > nsize:
                    break

                else:
                    #print '\n'.join([''.join(f) for f in top[1]])
                    #print "\n\n"
                    expansions = get_expansions(top[1], top[0])
                    for e in expansions:
                        if e not in sheap:
                            heappush(sheap, e)

            if ans is not None:
                return '\n'.join([''.join(f) for f in ans])

    return 'Impossible'


T = int(raw_input())

for t in xrange(T):
    tokens = raw_input().split()
    R = int(tokens[0])
    C = int(tokens[1])
    M = int(tokens[2])
    print "Case #%s:" % (t+1,)
    print solve(R, C, M)
