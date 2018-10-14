INFILE = 'E:\\cj\\' + 'A' + '.in.txt'
OUTFILE = 'E:\\cj\\A' + '.out'

fin = open(INFILE, 'r')
lines = fin.readlines()
fin.close()

fout = open(OUTFILE, 'w')

case = 0
cases = int(lines[0])
ptr = 1
for case in xrange(1, cases + 1):
    count = 0
    
    l = lines[ptr]
    ptr += 1
    N, M = map(int, l.split())
    D = {}
    for n in xrange(N):
        l = lines[ptr]
        ptr += 1
        dirs = l.strip().split('/')[1:]
        d = D
        for x in dirs:
            if x in d.keys():
                d = d[x]
            else:
                d[x] = {}
                d = d[x]            
    T = []
    for m in xrange(M):
        l = lines[ptr]
        ptr += 1
        T.append(l.strip().split('/')[1:])
    T.sort(lambda x, y: int.__cmp__(len(x), len(y)))
#    print T

    for t in T:
        d = D
        for x in t:
            if x in d.keys():
                d = d[x]
            else:
                d[x] = {}
                d = d[x]
                count += 1           
       
    fout.write('Case #%d: %d\n' % (case, count)) 

fout.close()
    
