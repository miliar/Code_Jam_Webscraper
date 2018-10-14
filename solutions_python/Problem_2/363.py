def toint(s):
    a, b = map(int, s.split(':'))
    return a*60+b

def solve():
    f = open('B-large.in')
    g = open('B.out','w')
    N = int(f.readline())
    for i in range(N):
        T = int(f.readline())
        NA, NB = map(int,f.readline().split())
        times = []
        for j in range(NA): times += [map(toint,map(str,f.readline().split()))+['a']]
        for j in range(NB): times += [map(toint,map(str,f.readline().split()))+['b']]
        times.sort()
        station = ''
        ctime = 0
        ret = {'a': 0, 'b': 0}
        sw = {'a': 'b', 'b': 'a'}
        while len(times):
            if station=='':
                t1,t2,c = times[0]
                ret[c] += 1
                times.pop(0)
                station = sw[c]
                ctime = t2 + T
            else :
                j = 0
                while j < len(times) :
                    t1,t2,c = times[j]
                    if c==station and ctime <= t1 :
                        times.pop(j)
                        station = sw[c]
                        ctime = t2 + T
                        break
                    j += 1
                else : station = ''
        g.write('Case #'+str(i+1)+': '+str(ret['a'])+' '+str(ret['b'])+'\n')
    g.close()
solve()