t = input()
for i in range(t):
    x, r, c = map(int, raw_input().split())
    ans = ''
    if x == 1:
        ans += 'GABRIEL'
    elif x == 2:
        if r % 2 == 0 or c % 2 == 0:
            ans += 'GABRIEL'
        else:
            ans += 'RICHARD'
    elif x == 3:
        if (r % 3 == 0 and c % 2 == 0) or (r % 2 == 0 and c % 3 == 0) or (r == 3 and c == 3):
            ans += 'GABRIEL'
        else:
            ans += 'RICHARD'
    elif x == 4:
        if (r % 3 == 0 and c % 4 == 0) or (r % 4 == 0 and c % 3 == 0) or (r % 4 == 0 and c % 4 == 0):
            ans += 'GABRIEL'
        else:
            ans += 'RICHARD'
    print 'Case #{0}: {1}'.format(i + 1, ans)
