f = open("in", "r")
fout = open("out", "w")
t = int(f.readline())
for tt in xrange(t):
    s_max, s = f.readline().split(' ')
    ans = 0
    count_up = 0
    for i in range(int(s_max) + 1):
        if i > count_up:
            ans += i - count_up
            count_up += i - count_up
        
        count_up += int(s[i])

    fout.write("Case #%d: %d\n" % (tt + 1, ans))
