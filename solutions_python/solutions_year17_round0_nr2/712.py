import sys

T = int(sys.stdin.readline().strip())

def is_tidy(n):
    for i in range(1, len(n)):
        if int(n[i]) < int(n[i-1]):
            return False
    return True
        
for t in range(1, T+1):
    N = sys.stdin.readline().strip()

    some = []
    if is_tidy(N):
        some.append(int(N))

    for i in range(1, len(N)):
        pref = str(int(N[:i]) - 1)
        ans = pref + '9' * (len(N) - i)
        ans = str(int(ans, 10))

        if is_tidy(ans):
            some.append(int(ans))

    print("Case #%d: %s" % (t, max(some)))
