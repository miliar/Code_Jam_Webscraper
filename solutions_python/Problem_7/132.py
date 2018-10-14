

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))


def generate_all_coords(n, A, B, C, D, x0, y0, M):
    """Generate all possible coordinates"""
    
    res=[]

    X, Y = x0, y0
    res.append((X, Y))
    for i in xrange(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        res.append((X, Y))
                
    return res

def temp_process(coords):
    for uc in xuniqueCombinations(coords, 3):
        xsum = ysum = 0
        for i in uc:
            xsum += i[0]
            ysum += i[1]


        if xsum % 3 == 0 and ysum % 3 == 0:
            print "Yes"


def process_data_files(fin, fout):
    """Read input data from 'fin' and write results into 'fout'"""

    N = int(fin.readline())

    for i in xrange(N):
        data=fin.readline().split(' ')
        n, A, B, C, D, x0, y0, M = map(lambda x: int(x), data)

        res = 0

        coords = generate_all_coords(n, A, B, C, D, x0, y0, M)

        for uc in xuniqueCombinations(coords, 3):
            xsum = ysum = 0
            for c in uc:
                xsum += c[0]
                ysum += c[1]


            if xsum % 3 == 0 and ysum % 3 == 0:
                res += 1


        fout.write("Case #%d: %d\n" % (i+1, res))
