def rank():
    ls1=[]
    seq=[]
    n=int(raw_input())
    for i in xrange(1,n*2):
        temp=map(int,raw_input().strip().split(' '))
        ls1+=temp
    ls1.sort()
    for i in list(set(ls1)):
        if ls1.count(i)%2!=0:
            seq.append(i)
        if len(seq)==n:
            break
    seq.sort()
    seq=map(str,seq)
    return ' '.join(seq)


for i in xrange(int(raw_input())):
    print "Case #%d: %s" % (i + 1, rank())