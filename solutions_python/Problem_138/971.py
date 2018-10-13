def parse_float(s):
    return int(s.split('.')[1].ljust(5,'0'))
def solve(A, B):
    B = B[:]
    for i, a in enumerate(A):
        nxt = next((b for b in B if b > a), None)
        if nxt is None:
            return len(A) - i
        else: B.remove(nxt)
    return 0
T = int(input())
for tc in range(T):
    n = int(input())
    A,B = [sorted(map(parse_float, input().split())) for _ in "aa"]
    print("Case #%d: %d %d" % (tc+1, n-solve(B,A), solve(A,B)))
