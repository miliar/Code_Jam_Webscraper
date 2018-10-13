

def lawnmower(a, n, m):
    s = []
    for i in range(n):
        for j in range(m):
            s.append((a[i][j], (i,j)))
    s.sort(reverse=True)
    r = [0 for i in range(n)]
    c = [0 for j in range(m)]
    for h, (i, j) in s:
        if r[i] > h and c[j] > h:
            return False
        if r[i] == 0:
            r[i] = h
        if c[j] == 0:
            c[j] = h
    return True



    #b = [[False for j in range(m)] for i in range(n)]
    #c = n * m
    #try:
        #for h, (i,j) in s:
            #if not b[i][j]:
                #b[i][j] = True  # unnecessary
                #c -= 1  # unnecessary
                #for k in range(n):
                    #if not b[k][j]:
                        #assert a[k][j] >= h
                        #b[k][j] = True
                        #c -= 1
                #for l in range(m):
                    #if not b[i][l]:
                        #assert a[i][l] >= h
                        #b[i][l] = True
                        #c -= 1
            #if c == 0:
                #break
    #except AssertionError:
        #return False
    #return True


def case(file):
    [n, m] = [int(x) for x in file.readline().strip().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in file.readline().strip().split()])
    if lawnmower(a, n, m):
        return "YES"
    else:
        return "NO"



def cases(in_name, func=None, out_name=None):
    if func is None:
        func = case
    if out_name is None:
        ext = in_name.rindex('.')
        out_name = in_name[:ext] + ".out"
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            ntests = int(fin.readline())
            for i in range(1, ntests + 1):
                fout.write("Case #%i: %s\n" % (i, func(fin)))

cases("B-large.in")