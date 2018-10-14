

def go(arr, n):
    top = ans = max(arr)
    for t in range(1, top):
        c = t
        for i in range(n):
            if arr[i] > t:
                c += (arr[i] - 1) / t
        ans = min(ans, c)
    return ans

T = int(raw_input())

for z in range(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print 'Case #{}: {}'.format(z + 1, go(arr, N))
