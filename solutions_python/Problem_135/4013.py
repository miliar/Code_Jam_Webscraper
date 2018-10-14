T = int(raw_input())
for i in xrange(T):
    count = 0
    row_one = int(raw_input()) - 1
    a = []
    for m in xrange(4):
        a.append(map(int,raw_input().split()))
    row_two = int(raw_input()) - 1
    b = []
    for n in xrange(4):
        b.append(map(int,raw_input().split()))
    for k in xrange(4):
        if b[row_two][k] in a[row_one]:
            ans = b[row_two][k]
            count += 1
    if count == 1:
       print "Case #%d: %d" %((i+1),ans)
    elif count > 1:
        print "Case #%d: Bad Magician!" %(i+1)
    else:
        print "Case #%d: Volunteer cheated!" %(i+1)
