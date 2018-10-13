import sys

def main(inp, pri, log):
    T = int(inp.readline())
    for t in xrange(T):
        N = int(inp.readline())
        ws = map(lambda f: map(int, inp.readline().strip().split()), xrange(N))
        log(ws)
        ws.sort(key=lambda (a, b): a)
        log(ws)
        res = 0
        for i in xrange(N - 1):
            for j in xrange(i + 1, N):
                if ws[j][1] < ws[i][1]:
                    res += 1
            
##        for di, ai, bi in ws:
##            if not di:
                
            
        print "Case #%d: %d" % (t+1, res)

if __name__ == "__main__":
    def makef(stream):
        def ans(s):
            if stream:
                print >> stream, s
        return ans
    if not sys.argv[0]:
        main(open('sample.in'), makef(sys.stdout), makef(sys.stdout))
    else:
        main(sys.stdin, makef(sys.stdout), makef(None))
