T = int(raw_input())

for i in xrange(T):

    msg = ['Bad magician!', 'Volunteer cheated!']
    sets = []
    for j in xrange(2):
        row = int(raw_input())
        st = set()
        for r in xrange(4):
            l = raw_input().split()
            if r+1 == row:
                st.update(l)
        sets.append(st)
    s = sets[0].intersection(sets[1])

    if len(s) == 0:
        code = 1
    elif len(s) == 1:
        ans = s.pop()
        msg.append(ans)
        code = 2
    else:
        code = 0

    print 'Case #%d: %s' %(i+1, msg[code])
