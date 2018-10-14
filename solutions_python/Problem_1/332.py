

def dofile(fname,outfname):
    result = dostr(file(fname).read())
    file(outfname,'w').write(result)

def dostr(s):
    dat = s.splitlines()

    #split to data sets
    N = int(dat[0])
    dat = dat[1:]
    
    results = []
    for i in xrange(N):
        S = int(dat[0])
        dat = dat[1:]
        engines = dat[:S]
        dat = dat[S:]
        Q = int(dat[0])
        dat = dat[1:]
        searches = dat[:Q]
        dat = dat[Q:]
        
        results.append(solve(engines,searches,i+1))

    return '\n'.join(results)


def find(x, l):
    return min([i for i in xrange(len(l)) if l[i]==x]+[len(l),])

def solve(engines,searches,ind):
    #pick first engine
    l = [find(x, searches) for x in engines]
    eng_ind = l.index(max(l))
    ret = 0

    while (l[eng_ind] < len(searches)):
        ret = ret+1
        searches = searches[l[eng_ind]:]
        l = [find(x, searches) for x in engines]
        eng_ind = l.index(max(l))

    return "Case #%d: %d" % (ind, ret)
    

            
