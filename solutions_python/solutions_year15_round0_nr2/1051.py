import heapq

def main(ifn='bin.txt',ofn='bout.txt'):
    with open(ifn) as inf:
        with open(ofn,'w') as ouf:
            T = int(inf.readline().strip())
            for tn in xrange(1,T+1):
                d = int(inf.readline().strip())
                c = [int(x.strip()) for x in inf.readline().strip().split(' ') if len(x.strip())>0]
                assert(len(c)==d)
                res = max(c)
                cnt = 1
                while cnt<res:
                    tmp = sum([(x-1)/cnt for x in c])+cnt
                    if tmp<res:
                        res = tmp
                    cnt += 1
                ouf.write('Case #%d: %d\n' %(tn,res))

if __name__=='__main__':
    main()
