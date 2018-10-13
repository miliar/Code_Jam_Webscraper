def solve(s, n):
    s = [c == '+' for c in s]
    n, cnt = int(n), 0

    while True:
        try:
            s = s[s.index(False):]
        except ValueError:
            break

        for i in range(n):
            try:
                s[i] = not s[i]
            except IndexError:
                return 'IMPOSSIBLE'
        cnt += 1

        if len(s) <= n and False in s:
            return 'IMPOSSIBLE'

    return cnt

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, solve(*input().split())))
