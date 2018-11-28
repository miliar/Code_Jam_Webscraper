import sys
if __name__ == '__main__':
    input_filename, = sys.argv[1:]
    input = open(input_filename)
    assert input_filename.endswith('.in'), input_filename
    output = open(input_filename[:-3]+'.out', 'w')

def find_adjacences((i,j)):
    yield (i+1, j)
    yield (i, j+1)
    yield (i-1, j)
    yield (i, j-1)

def new_canvas(n, m):
    return [['.'] * m for i in range(n)]

def copy_canvas(canvas):
    return [line[:] for line in canvas]

def put(o, canvas, (x, y)):
    R = len(canvas)
    C = len(canvas[0])
    for p in o:
        assert p[0]>=0 and p[1]>=0
        p = (x+p[0], y+p[1])
        if p[0]<0 or p[1]<0 or p[0] >= C or p[1] >=R:
            return False  # esce fuori
        if canvas[p[1]][p[0]] == '.':
            canvas[p[1]][p[0]] = '#'
        else:
            return False
    return True

def write(o):
    max_x = max([p[0] for p in o])
    max_y = max([p[1] for p in o])
    canvas = new_canvas(max_y+1, max_x+1)
    r = put(o, canvas, (0, 0))
    assert r
    canvas = [''.join(x) for x in canvas]
    print '\n'.join(canvas)
    
def normalized(o):
    min_x = min([p[0] for p in o])
    min_y = min([p[1] for p in o])
    return frozenset([(x-min_x, y-min_y) for (x,y) in o])

def all_ominoes(n):
    if n == 1:
        return set([frozenset([(0,0)])])
    found = set()
    for o in all_ominoes(n-1):
        for p in o:
            for a in find_adjacences(p):
                if not a in o:
                    oo = normalized(o.union([a]))
                    found.add(oo)
    return found

def solve_(ominoes, canvas, depth = 0):
    # restituisce l'insieme di tutti gli ominoes che possono essere utilizzati per completare il canvas
    # oppure False se non si puo' completare
    print ' '*depth + 'solve_', canvas
    used = set()
    R = len(canvas)
    C = len(canvas[0])
    for x in range(C):
        for y in range(R):
            if canvas[y][x] == '.':
                # trovata "prima" casella libera
                # per vedere se lo schema si puo' completare
                # provo a mettere qui ogni ominous in ogni posizione
                for o in ominoes:
                    for p in o:
                        # e' possibile aggiungere o con p in posizione (x,y)?
                        c = copy_canvas(canvas)
                        if put(o, c, (x-p[0], y-p[1])):
                            u = solve_(ominoes, c, depth = depth + 1)
                            if u is not False:
                                used = used.union(u)
                                used.add(o)
                if not used:
                    print ' '*depth + '= FAIL!'
                    return False  # no solution found
                print ' '*depth + '= ', list(map(list, used))
                return used

    print ' '*depth + '= filled!'
    return used  # empty, but enough
            

def solve():
    X, R, C = map(int, input.readline().strip().split())
    print X, R, C
    ominoes = all_ominoes(X)
    canvas = new_canvas(R, C)
    used = solve_(ominoes, canvas) or set()
    if C != R:
        canvas = new_canvas(C, R)
        used = used.union(solve_(ominoes, canvas) or set())
    return {False: 'RICHARD', True: 'GABRIEL'}[len(used) == len(ominoes)]


if __name__ == '__main__':
    for o in all_ominoes(4):
        write(o)
        print


    T = int(input.readline())
    
    for t in range(T):
        print >> output, 'Case #%s: %s' % (t+1,solve())
