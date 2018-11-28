for cas in range(int(raw_input())):
    n, a = int(raw_input()) - 1, [raw_input().split() for i in range(4)]
    m, b = int(raw_input()) - 1, [raw_input().split() for i in range(4)]
    ans = filter(lambda x: x[0] == x[1], [(i, j) for i in a[n] for j in b[m]])
    print "Case #%d: %s" % (cas + 1, "Volunteer cheated!" if len(ans) == 0 else ans[0][0] if len(ans) == 1 else "Bad Magician!")
