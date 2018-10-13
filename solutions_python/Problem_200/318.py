def run(s):
    flag = True
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            flag = False
            s[i-1] = chr(ord(s[i-1]) - 1)
            for j in range(i, len(s)):
                s[j] = '9'
            break
    return flag

T = int(raw_input().strip())

for t in range(1, T + 1):
    s = list(raw_input().strip())
    while not run(s):
        pass
    print 'Case #%s: %s' % (t, ''.join(s).lstrip('0'))
