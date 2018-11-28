

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
        T = int(dat[0])
        dat = dat[1:]
        (NA,NB) = map(int, dat[0].split(' '))
        dat = dat[1:]
        A = dat[:NA]
        dat = dat[NA:]
        B = dat[:NB]
        dat = dat[NB:]
        results.append(solve(A,B,T,i+1))

    return '\n'.join(results)

def hour2min(s):
    (HH,MM) = map(int, s.split(':'))
    return 60*HH+MM


def solve(A,B,T,ind):
    print A,B,T,ind
    Bin = [hour2min(x.split(' ')[1])+T for x in A]
    Ain = [hour2min(x.split(' ')[1])+T for x in B]

    Bout = [hour2min(x.split(' ')[0]) for x in B]
    Aout = [hour2min(x.split(' ')[0]) for x in A]

    Bin.sort()
    Ain.sort()
    Bout.sort()
    Aout.sort()


    Bres = 0
    Ares = 0

    for i in range(len(Bout)):
        Bres = max(Bres, i+1-len([x for x in Bin if x <= Bout[i]]))
    for i in range(len(Aout)):
        Ares = max(Ares, i+1-len([x for x in Ain if x <= Aout[i]]))
    
    return "Case #%d: %d %d" % (ind, Ares, Bres)
    

            
