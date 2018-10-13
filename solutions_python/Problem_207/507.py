def validate(s):
    pass

def solver(line):
    n,r,o,y,g,b,v = line
    t1 = b - o
    t2 = y - v
    t3 = r - g
    if t1 < 0 or t2 < 0 or t3 < 0:
        return "IMPOSSIBLE"
    if 0 in [t1,t2,t3]:
        if line[1:].count(0) == 4:
            L = [(r,'R'),(o,'O'),(y,'Y'),(g,'G'),(b,'B'),(v,'V')]
            L.sort(key = lambda x: -x[0])
            if L[0][0] == L[1][0]:
                return (L[0][1] + L[1][1]) * L[0][0]
            else:
                return "IMPOSSIBLE"
        else:
            return "IMPOSSIBLE"
    L = [t1,t2,t3]
    if sum(L) < 2 * max(L):
        return "IMPOSSIBLE"
    else:
        L = [[t1,'B'],[t2,'Y'],[t3,'R']]
        s = '_'
        while sum(i[0] for i in L) > 3:
            #error: haven't enforced start != end
            L.sort(key = lambda x: -x[0])
            if L[0][1] != s[-1]:
                s += L[0][1]
                L[0][0] -= 1
            else:
                s += L[1][1]
                L[1][0] -= 1
                if L[1][0] < 0:
                    print "bad stuff"
        s = s[1:]
        if s:
            t = s[0] + s[-1]
        else:
            t = 'RR'
        d = {'RR' : 'BRY',
             'RY' : 'BRY',
             'RB' : 'YRB',
             'YR' : 'BYR',
             'YY' : 'BYR',
             'YB' : 'RYB',
             'BR' : 'YBR',
             'BY' : 'RBY',
             'BB' : 'RBY'}
        s += d[t]    
        s = s.replace('B','BO' * o + 'B', 1)
        s = s.replace('Y','YV' * v + 'Y', 1)
        s = s.replace('R','RG' * g + 'R', 1)
        return s

#case testing needs to happen


fout = open('out.txt','w')
f = open('in.txt')

T = int(f.readline())
for case in range(1,T+1):
    line = f.readline()

    line = line.split()
    line = [int(i) for i in line]
    ans = solver(line)

    
    
    str = "Case #%d: %s\n" % (case, ans)
    print str,
    fout.write(str)

f.close()
fout.close()
