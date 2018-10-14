def method1(N, M):
    return sum(map(lambda (a, b): max(0, a-b), zip(M, M[1:])))

def method2(N, M):
    rate = max(map(lambda (a, b): max(0, a-b), zip(M, M[1:])))
    total = sum(map(lambda a: min(a, rate), M[:-1]))
    return total

def solve(N, M):
    return str(method1(N, M)) + " " + str(method2(N, M))

for _t in range(1, 1+int(raw_input())):
    N = int(raw_input())
    M = map(int, raw_input().strip().split())
    print "Case #%d: %s" % (_t, solve(N, M))
