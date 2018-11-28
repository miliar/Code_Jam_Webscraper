import sys

T = int(sys.stdin.readline())

def test():
    N = list(map(int, sys.stdin.readline().strip()))
    i = len(N) - 2
    while True:
        if i < 0: break
        if N[i] > N[i+1]:
            N[i] -= 1
            N[i+1:] = [9] * (len(N) - i - 1)
        i -= 1
    return ''.join(map(str, N))


for t in range(T):
    ans = test()
    print('Case #{}: {}'.format(t+1, ans.lstrip('0')))
