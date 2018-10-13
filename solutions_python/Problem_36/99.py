name = 'C'
typ = 'large'
base = name+'-'+typ+'.'
vstup = file(base+'in').read()

lines = vstup.split('\n')
N = int(lines[0])

pattern = 'welcome to code jam'

def solve(test, ti=0, pi=0):
    if pi == len(pattern): return 1
    if cache[ti][pi] != -1:
        return cache[ti][pi]
    start_at = ti-1
    ret = 0
    while True:
        start_at = test.find(pattern[pi],start_at+1)
        if start_at == -1: break
        ret += solve(test,start_at,pi+1)
        ret %= 10000
    cache[ti][pi] = ret
    return ret

vystup = file(base+'out','w')
i = 1
for test in lines[1:N+1]:
    cache = [[-1 for c1 in xrange(len(pattern))] for c2 in xrange(len(test))]

    vystup.write('Case #'+str(i)+': '+str(solve(test)).rjust(4,'0')+'\n')
    i += 1
vystup.close()
