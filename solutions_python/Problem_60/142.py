
def do_case(N,K,B,T,chicks):
    if sum([chick[0]+chick[1]*T>=B for chick in chicks]) < K:
        return "IMPOSSIBLE"
    nc = [chick[0]+chick[1]*T for chick in chicks]
    sw = 0
    nc = nc[::-1]
    for i in xrange(K):
        if nc[i] < B:
            for j in xrange(i+1,len(chicks)):
                if nc[j] >= B:
                    nc[i],nc[j] = nc[j],nc[i]
                    sw += (j - i)
                    break
    return sw
    
def do(inp):
        lines = inp.split('\n')
        C = int(lines[0])
        cases = lines[1:]
        result = ""
        for t in range(C):
                N,K,B,T = map(int,cases.pop(0).split(' '))
                Xs = map(int,cases.pop(0).split(' '))
                Vs = map(int,cases.pop(0).split(' '))
                chicks = zip(Xs,Vs)
                answer = do_case(N,K,B,T,chicks)
                result += "Case #%s: %s\n" % (str(t+1),answer)
        return result
        
if __name__ == '__main__':
    filename = 'B-large'
    #filename = 'mini2'
    inp = open('%s.in' % filename).read()
    r = do(inp)
    open('%s.out' % filename,'w').write(r)

