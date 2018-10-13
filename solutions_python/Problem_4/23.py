
def MinScalarProduct():
    n = int(raw_input())
    X = map(int, raw_input().split())
    Y = map(int, raw_input().split())
    X.sort()
    Y.sort(reverse=True)
    result = 0
    for x, y in zip(X, Y):
        result += x * y
    print result

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase + 1),
    MinScalarProduct()
