T = input()

for case in range(T):
    input() # N
    Es = [int(x) for x in raw_input().split()]
    ans = 0.0
    for i,j in enumerate(Es):
        if i+1 != j:
            ans += 1

    print "Case #%i: %f" % (case + 1, ans)
