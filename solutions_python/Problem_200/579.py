import sys


def largest_tidy(N):
    A = map(int, str(N))
    tidy = True
    carry = False
    for i in range(len(A) - 1, 0, -1):
        if A[i] < A[i - 1]:
            for j in range(i, len(A)):
                A[j] = 9
            A[i - 1] -= 1
    return int(''.join(map(str, A)))

T = int(raw_input().strip())

for i in range(1, T + 1):
    N = int(raw_input().strip())
    t = largest_tidy(N)
    print 'Case #%d: %d' % (i, t)
