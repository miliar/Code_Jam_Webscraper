
T = int(raw_input())
for cas in xrange(1,T+1):
    m = int(raw_input())
    st1 = [set(),set(),set(),set()]
    st2 = [set(),set(),set(),set()]
    for i in xrange(4):
        st1[i] = set(map(int,raw_input().split(' ')))
    n = int(raw_input())
    for i in xrange(4):
        st2[i] = set(map(int,raw_input().split(' ')))
    
    m-=1
    n-=1
    res = list(st1[m].intersection(st2[n]))
    if len(res) == 1:
        print 'Case #%d: %d'%(cas,res[0])
    elif len(res) == 0:
        print 'Case #%d: Volunteer cheated!'%(cas,)
    elif len(res) > 1:
        print 'Case #%d: Bad magician!'%(cas,)
    
    



