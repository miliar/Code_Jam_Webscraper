
def SavingTheUniverse():
    S = int(raw_input())
    x = dict()
    for i in range(S):
        name = raw_input()
        x[name] = 0
    nn = S
    result = 0
    Q = int(raw_input())
    for i in range(Q):
        name = raw_input()
        if x[name] == result:
            nn -= 1
            if nn == 0:
                nn = S - 1
                result += 1
            x[name] = result + 1
    print result

N = int(raw_input())
for testcase in range(N):
    print "Case #%d:" % (testcase + 1),
    SavingTheUniverse()
