def find_not_tidy_pos(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return i + 1
    return None


def downgrade(s, pos):
    for i in range(pos, len(s)):
        s[i] = '9'
    i = pos - 1
    while i > 1 and s[i] == '0':
        s[i] = '9'
        i -= 1
    s[i] = str(int(s[i]) - 1)

    while s[0] == '0':
        s = s[1:]
    return s


def solve(s):
    pos = find_not_tidy_pos(s)
    while pos is not None:
        s = downgrade(s, pos)
        pos = find_not_tidy_pos(s)
    return s

for t in range(1, int(raw_input()) + 1):
    n = list(raw_input().strip())
    sol = solve(n)
    print 'Case #%d: %s' % (t, ''.join(sol))