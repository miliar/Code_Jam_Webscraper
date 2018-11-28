def add_first_letter(s, cnt):
    max_val = max((cnt[letter], letter) for letter in 'RYB')
    if max_val[0] <= 0:
        raise ValueError
    s += max_val[1]
    cnt[max_val[1]] -= 1
    return s

def add_letter(s, cnt, permitted):
    max_val = max((cnt[letter], letter) for letter in filter(lambda x: x != permitted, 'RYB'))
    if max_val[0] <= 0:
        raise ValueError
    s += max_val[1]
    cnt[max_val[1]] -= 1
    return s

def solve(test_case):
    n, R, O, Y, G, B, V = map(int, input().split())
    s = ''
    cnt = {'R': R, 'Y': Y, 'B': B}
    s = add_first_letter(s, cnt)
    for i in range(n - 1):
        try:
            s = add_letter(s, cnt, s[-1])
        except ValueError:
            print("Case #%d: %s" % (test_case + 1, 'IMPOSSIBLE'))
            return
    if s[0] == s[-1]:
        l = list(map(lambda x: x, s))
        if s[0] != s[-2] and s[-1] != s[-3]:
            l[-1], l[-2] = l[-2], l[-1]
        else:
            v = [s[0], s[-2]]
            for i in range(1, len(s) - 2):
                if (s[i] not in v) and (s[-1] not in s[i - 1:i + 2]):
                    l[i], l[-1] = l[-1], l[i]
                    break
        s = ''.join(l)
    if s[0] == s[-1] and len(s) != 1:
        print("Case #%d: %s" % (test_case + 1, 'IMPOSSIBLE'))
    else:
        print("Case #%d: %s" % (test_case + 1, s))

def main():
    t = int(input())
    for i in range(t):
        solve(i)

main()
