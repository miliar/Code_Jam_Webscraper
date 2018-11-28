from sys import stdin

def tidy_prefix(s):
    t  = '0' + s + '0'
    for i in range(1, len(t)):
        if t[i] < t[i-1]:
            return s[:i-1]

def make_tidy(s, l):
    if len(s) == l:
        return s
    p = s.rstrip(s[-1])
    if p == '' and s[0] == '1':
        return (l-1)*'9'
    p = p + str(int(s[-1])-1)
    return p + (l-len(p))*'9'

data = stdin.readlines()

for i, line in enumerate(data[1:], 1):
    case = line.strip()
    tp = tidy_prefix(case)
    res = make_tidy(tp, len(case))
    print('Case #{}: {}'.format(i, res))
