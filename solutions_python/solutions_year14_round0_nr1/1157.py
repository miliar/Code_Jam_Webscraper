T = input()

for casenbr in range(T):
    a1 = input() - 1
    m1 = []
    for i1 in range(4):
        m1.append(raw_input().strip().split())

    a2 = input() - 1
    m2 = []
    for i1 in range(4):
        m2.append(raw_input().strip().split())

    s = set(m1[a1]) & set(m2[a2])
    ans = 'Volunteer cheated!'
    if s:
        if len(s) > 1:
            ans = 'Bad magician!'
        else:
            ans = s.pop()

    print "Case #%d: %s" % (casenbr+1, ans)
