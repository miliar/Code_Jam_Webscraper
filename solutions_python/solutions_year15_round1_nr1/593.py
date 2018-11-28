T = input()
for tt in range(T):
    n = input()
    m = map(int, raw_input().split())
    first, second = 0, 0
    temp = 0
    for i in range(n - 1):
        first += max(0, m[i] - m[i+1])
        temp = max(temp, m[i] - m[i+1])
    for i in range(n - 1):
        second += min(temp, m[i])
    print "Case #%d: %d %d"% ((tt + 1),
                         first, second)
