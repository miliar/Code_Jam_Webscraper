def do(inp):
        lines = inp.split('\n')
        T = int(lines[0])
        cases = lines[1:]
        result = ""
        for t in xrange(T):
                R,k,n = map(int,cases.pop(0).split(' '))
                q = map(int,cases.pop(0).split(' '))
                cache ={}
                for i in xrange(len(q)):
                        minisum = 0
                        j = i
                        while j-i<len(q) and minisum+q[j%len(q)] <= k:
                                minisum += q[j%len(q)]
                                j += 1
                        cache[i] = (minisum,j%len(q))
                monies = 0
                idx = 0
                for i in xrange(R):
                        extra,idx = cache[idx]
                        monies += extra
                result += "Case #%s: %s\n" % (str(t+1),monies)
        return result
        
if __name__ == '__main__':
    filename = 'C-small-attempt0'   
    inp = open('%s.in' % filename).read()
    r = do(inp)
    open('%s.out' % filename,'w').write(r)

