T = int(raw_input())
for t in range(T):
    A = int(raw_input())
    rows = []
    for a in range(4):
        rows.append(raw_input())
    Arow = rows[A-1]
    Arow = [int(i) for i in Arow.split()]
    
    B = int(raw_input())
    rows = []
    for b in range(4):
        rows.append(raw_input())
    Brow = rows[B-1]
    Brow = [int(i) for i in Brow.split()]

    ans = []
    for a in Arow:
        if a in Brow:
            ans.append(a)

    if len(ans) == 1:
        print 'Case #%s: %s' % (t+1, ans[0])
    elif len(ans) == 0:
        print 'Case #%s: Volunteer cheated!' % (t+1)
    else:
        print 'Case #%s: Bad magician!' % (t+1)
