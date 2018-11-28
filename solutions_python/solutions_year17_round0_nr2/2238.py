num = int(raw_input())
for i in range(1,num+1):
    tt = raw_input().split(" ")
    tt = tt[0]

    borrow = False
    for j in range(1, len(tt)):
        ind = len(tt) - j

        if tt[ind] < tt[ind - 1]:
            tt = str(int(tt[:ind]) - 1) + "9" * j
            borrow = True

    tt = tt.lstrip("0")
    print "Case #%d: %s"  %(i, tt)
