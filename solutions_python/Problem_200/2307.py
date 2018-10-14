T = input()

def solve():
    A = map(int, list(raw_input()))
    index = len(A) - 1
    start = -1
    while index > 0:
        prev = index - 1
        if A[prev] > A[index]:
            A[prev] -= 1
            start = prev
        index -= 1
    if start != -1:
        for i in xrange(start+1, len(A)):
            A[i] = 9
    return int(''.join(map(str, A)))

for t in range(T):
    ans = solve()
    print 'Case #{0}: {1}'.format(t+1, ans)
