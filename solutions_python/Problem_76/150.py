
def CandySplitting():
    raw_input()
    s, x = 0, 0
    m = 123456789
    for value in map(int, raw_input().split()):
        s += value
        x ^= value
        m = min(value, m)
    if x:
        print "NO"
    else:
        print s-m

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    CandySplitting()
