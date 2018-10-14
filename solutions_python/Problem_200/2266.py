T = int(raw_input())

def solve(n):
    ans = n
    for i in range(1, len(n)):
        if int(n[i]) < int(n[i - 1]):
            ans = n[:i - 1] + str(int(n[i - 1]) - 1) + '9' * len(n[i:])
            break
    start = 0
    while start < len(ans) and ans[start] == '0':
        start += 1
    return ans[start:]

for i in range(T):
    N = raw_input()
    while True:
        tn = solve(N)
        if tn == N:
            print "Case #" + str(i + 1) + ": " + tn
            break
        N = tn
