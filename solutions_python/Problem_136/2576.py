t = int(raw_input())
st_pace = 2
for case_nr in xrange(1, t + 1):
    pace = st_pace
    c, f, x = map(float, raw_input().strip().split())
    ans = x / pace
    t_ans = c / pace
    while t_ans < ans:
        pace += f
        if ans > t_ans + x / pace:
            ans = t_ans + x / pace
        t_ans += c / pace
    print "Case #%d: %.7f" % (case_nr, ans)
