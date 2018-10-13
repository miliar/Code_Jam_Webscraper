import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        quit()

    fname = sys.argv[1]
    if len(sys.argv) > 2:
        ofname = sys.argv[2]
    else:
        ofname = 'unitc.out'
    
    try:
        infile = open(fname)
        outfile = open(ofname, 'w')
        T = int(infile.readline().strip())
        
        for t in range(1, T+1):
            N, K = map(int, infile.readline().strip().split())
            print N, K
            ranges = {N: 1}

            n = 1
            nn = 1
            while True:
                if nn >= K:
                    K -= n
                    break
                n = nn
                nranges = {}
                for k in ranges.keys():
                    d = k - 1
                    nk = d / 2
                    if nk in nranges:
                        nranges[nk] += ranges[k]
                    else:
                        nranges[nk] = ranges[k]
                    
                    nk = d / 2 + (d & 1)
                    if nk in nranges:
                        nranges[nk] += ranges[k]
                    else:
                        nranges[nk] = ranges[k]
                ranges = nranges
                nn = n * 2 + 1
            l = reversed(sorted(ranges.keys()))
            k = l.next()
            while K > ranges[k]:
                K -= ranges[k]
                k = l.next()
            r = k - 1
            lsmin, lsmax = r / 2, r / 2 + (r & 1)
            res = 'Case #%d: %d %d' % (t, lsmax, lsmin)
            print res
            outfile.write(res)
            outfile.write('\n')
        infile.close()
        outfile.close()
            
    except Exception as e:
        print 'Error:', e
        import traceback
        traceback.print_exc()
