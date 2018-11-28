def row(r):
    last = '?'
    for i in range(len(r)):
        if r[i] == '?':
            r[i] = last
        else:
            last = r[i]
    i = 0
    while i < len(r) and r[i] == '?':
        i += 1
    if i < len(r):
        last = r[i]
        while i >= 0:
            r[i] = last
            i -= 1
    return r

def solve(test_num):
    r, c = map(int, input().split())
    s = [row(list(input())) for i in range(r)]
    last = s[0]
    for i in range(r):
        if s[i][0] == '?':
            s[i] = last
        else:
            last = s[i]
    i = 0
    while s[i][0] == '?':
        i += 1
    last = s[i]
    while i >= 0:
        s[i] = last
        i -= 1
    print("Case #", test_num, ":", sep='')
    for line in s:
        print("".join(line))

for i in range(1, int(input()) + 1):
    solve(i)

