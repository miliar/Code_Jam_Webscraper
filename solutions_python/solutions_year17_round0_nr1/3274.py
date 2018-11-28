def flip(inp):
    s, k = inp.split(' ')
    k = int(k)
    s = list(s)
    if s.count('-') == 0:
        return '0'
    count = 0
    try:
        while s.count('-'):
            cursor = s.index('-')
            for i in range(cursor, cursor + k):
                if s[i] == '+':
                    s[i] = '-'
                else:
                    s[i] = '+'
            count += 1
        return str(count)
    except IndexError:
        return 'IMPOSSIBLE'


for i in range(int(input().strip())):
    print("Case #%d: %s" % (i + 1, flip(input().strip())))
