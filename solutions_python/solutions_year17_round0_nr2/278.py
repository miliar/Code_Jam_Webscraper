# lizesheng
#


def solve(s):
    s = [int(d) for d in s]

    ok = False
    while not ok:
        for i, d in enumerate(s):
            if i+1 != len(s):
                if d > s[i+1]:
                    s[i] -= 1
                    s[i+1:] = [9]*len(s[i+1:])
                    break
                else:
                    continue
            else:
                ok = True

    for j in range(len(s)):
        if s[j] != 0:
            break
    s = s[j:]

    return ''.join(str(d) for d in s)


t = int(input())
for icase in range(1, t + 1):
    a = input()
    print("Case #{}: {}".format(icase, solve(a)))
