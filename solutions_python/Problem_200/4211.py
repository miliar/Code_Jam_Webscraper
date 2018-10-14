T = int(raw_input())

for i in xrange(0,T):
    N = raw_input()
    ind = -1
    while int(N) != int("".join(sorted(N))):
        lst = list(N)
        lst[ind] = "9"
        lst[ind-1] = str(int(lst[ind-1]) - 1)
        ind -= 1
        while int(lst[ind]) < 0:
            lst[ind-1] = str(int(lst[ind-1]) - 1)
            lst[ind] = "9"
            ind -= 1
        N = "".join(lst)
    print "Case #" + str(i+1) + ": " + str(int(N))