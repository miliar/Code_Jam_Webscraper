f=open('A-large.in', 'r')
T=int(f.readline());

for casecount in xrange(1,T+1):
    l2=f.readline()
    l2=map(lambda x: int(x),l2.split())
    N=l2[0]
    K=l2[1]
    state=2**N-1
    if ((K+1) % (state+1))==0:
        print "Case #%d: ON" % casecount
    else:
        print "Case #%d: OFF" % casecount

f.close()
