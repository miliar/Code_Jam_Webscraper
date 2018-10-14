#casename = 'sample'
#casename = 'small'
casename = 'large'

def solve():
    fi = open('goro_'+casename+'_in.txt','r')
    fo = open('goro_'+casename+'_out.txt','w')
    T = int(fi.readline())
    for t in xrange(1,T+1):
        N = int(fi.readline())
        x = map(int,fi.readline().strip().split())
        fo.write("Case #%d: %.6f\n"%(t,float(len(x)-sum([x[i]==i+1 for i in range(len(x))]))))
    fi.close()
    fo.close()
        
