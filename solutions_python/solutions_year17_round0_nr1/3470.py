def flip(s, k, i):
    return s[0:i] + ''.join(map(lambda c: c == '+' and '-' or '+', s[i:i+k])) + s[i+k:]

def check(s):
    return len(filter(lambda c: c == '+', s)) == len(s)

def get_flips(s, k):
    i = 0
    f = 0

    while (i <= len(s)-k):
        if (s[i] == '-'):
            s = flip(s, k, i)
            f += 1
            i += 1
        else:
            i += 1

    if (check(s)):
        return f
    else:
        return -1

def fix_case(n, s, k):
    f = get_flips(s, k)

    if (f != -1):
        print('Case #%d: %d'%(n, f))
    else:
        print('Case #%d: IMPOSSIBLE'%(n))

def run(input):
    lines = str.split(input, '\n')[1:]
    for i in xrange(len(lines)):
        s, k = str.split(lines[i], ' ')
        fix_case(i+1, s, int(k))

if __name__ == '__main__':
    with open('A-large.in', 'r') as myfile:
        input = myfile.read().strip()
        run(input)
