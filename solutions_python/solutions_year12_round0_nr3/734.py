
N = int(raw_input())



for case in xrange(0, N):
    a, b = map(int, raw_input().split(" "))
    count = 0
    remember = {}
    for x in xrange(a, b + 1):
        A = str(x)
        for divider in xrange(1, len(A)):
            check = int(A[divider:] + A[:divider])
            if check <= b and check > x:
                if str(check) + str(x) in remember:
                    continue
                remember[str(check) + str(x)] = True
                count = count + 1
    print "Case #" + str(case + 1) + ": " + str(count)

