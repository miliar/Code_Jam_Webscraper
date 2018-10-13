from fileinput import input

def flip(pancakes, i, k):
    for j in range(i, i+k):
        pancakes[j] = not pancakes[j]

case = 1
for _ in range(int(raw_input())):
    pancakes, k = raw_input().split()
    pancakes = [p == '+' for p in pancakes]
    k = int(k)
    n = len(pancakes)

    _pan = pancakes[:]
    i = 0
    cnt1 = 0
    while i <= n-k:
        if not _pan[i]:
            flip(_pan, i, k)
            cnt1 += 1
        i += 1

    if not all(_pan):
        cnt1 = float('inf')

    _pan = pancakes
    i = n-1
    cnt2 = 0
    while i >= k-1:
        if not _pan[i]:
            flip(_pan, i-k, k)
            cnt2 += 1
        i -= 1

    if not all(_pan):
        cnt2 = float('inf')

    m = min(cnt1, cnt2)
    if m == float('inf'):
        print 'Case #{0}: IMPOSSIBLE'.format(case)
    else:
        print 'Case #{0}: {1}'.format(case, m)
        
    case += 1
