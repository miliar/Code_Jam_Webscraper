def get(pos, last, n):
    if pos == len(n):
        return 0

    cur = ord(n[pos]) - ord('0')
    pw = len(n) - pos - 1
    if cur < last:
        return -1

    t = get(pos + 1, cur, n)
    if t != -1:
        t = cur * 10 ** pw + t
        return t

    if cur - 1 >= last:
        t = (cur - 1) * 10 ** pw
        if pw > 0:
            t += 10 ** pw - 1
        return t
    return -1

    

def solve(test):
    n = input()

    print('Case #{}: {}'.format(test, get(0, 0, n)))



t = int(input())
for i in range(t):
    solve(i + 1)
