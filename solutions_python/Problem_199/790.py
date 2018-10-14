flip = {'-':'+', '+':'-'}
num_cases = int(raw_input())
for case in range(num_cases):
    s = raw_input()
    K = int(s.split()[-1])
    s = list(s.split()[0])

    ans = 0
    for i in range(len(s)-K+1):
        if s[i] == '-':
            ans += 1
            for j in range(K):
                s[i+j] = flip[s[i+j]]

    print 'Case #%d:' % (case+1),
    if all(c == '+' for c in s):
        print ans
    else:
        print 'IMPOSSIBLE'
