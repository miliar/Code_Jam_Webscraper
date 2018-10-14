def solve(n):
    l = len(n)
    if l == 1: return n
    res = [int(n[i]) for i in range(l)]
    pos = l-1
    i = 0
    while i < pos:
        if res[i] > res[i+1]:
            res[i] -= 1
            pos = i
            i = 0
        else:
            i += 1
    result = ''.join(str(res[i]) for i in range(pos+1)) + '9' * (l-pos-1)
    return result.lstrip('0')


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n = str(input())
        res = solve(n)
        print("Case #{}: {}".format(i, res))