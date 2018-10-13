import psyco
psyco.full()

def main():
    f = open('A-large.in')
    fo = open('A-large.out','w')

    X = int(f.next().strip())
    for x in xrange(X):
        N, K = [int(i) for i in f.next().strip().split()]
        num = 2**N
        tmp = K % num
        if tmp == num -1:
            fo.write('Case #%d: ON\n'%(x+1))
        else:
            fo.write('Case #%d: OFF\n'%(x+1))
    f.close()
    fo.close()
                     
        
main()
