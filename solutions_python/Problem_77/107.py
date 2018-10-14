T = int(raw_input())

for case in xrange(1, T+1):
    raw_input()
    numbers = map(int, raw_input().split())
    ans = len(numbers)
    for i in xrange(len(numbers)):
        if numbers[i] == i+1:
            ans -= 1
    print "Case #%d: %d.000000"%(case, ans)

