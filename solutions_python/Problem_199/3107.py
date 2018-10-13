for t in range(int(input())):
    s, k = input().split()
    k = int(k)
    ans = 'IMPOSSIBLE'
    flips = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            flips += 1
            s = s[:i] + ''.join(['-' if x == '+' else '+' for x in s[i:i+k]]) + s[i+k:]
    print('Case #%d: %s' % (t+1, 'IMPOSSIBLE' if '-' in s else flips))
