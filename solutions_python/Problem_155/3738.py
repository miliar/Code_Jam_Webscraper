from multiprocessing import Pool

def parse(line, Cn):
    Smax = int(line[0])
    Slist = [0] * (Smax + 1)
    for i, Si in enumerate(line[2:]):
        Slist[i] = int(Si)
        
    return (Cn, solve(Slist))
    
def solve(Slist):
    Scur = 0
    Sfriend = 0
    for i, Sn in enumerate(Slist):
        if i <= Scur:
            Scur += Sn
        else:
            Fn = i - Scur
            Sfriend += Fn
            Scur += Fn + Sn
    return Sfriend
        

pool = Pool()

lines = int(raw_input())

result = [0] * lines

def getResult(r):
    result[r[0]-1] = r[1]


for l in range(1,lines+1):
    line = raw_input()
    pool.apply_async(parse, [line,l], callback=getResult)
    
pool.close()
pool.join()

for i,r in enumerate(result):
    print "Case #%i: %i" % (i+1, r)