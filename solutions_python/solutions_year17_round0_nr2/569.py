
def solve():
    n = list(input())
    idx = -1
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            idx = i
            break
    if idx != -1:
        pos = 0
        for i in range(1, idx):
            if n[i - 1] < n[i]:
                pos = i
        n[pos] = chr(ord(n[pos]) - 1)
        for i in range(pos + 1, len(n)):
            n[i] = '9'
    print(int(''.join(n)))

T = int(input())
for t in range(T):
    print("Case #%d: " % (t + 1), end='')
    solve()
