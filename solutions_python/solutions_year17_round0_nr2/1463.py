from math import log10, ceil

TEST = False

def read(file):
    if TEST:
        return input()
    return file.readline()

def write(s, file):
    if TEST:
        print(s)
    else:
        print(s, file=file)

def is_tidy(n):
    s = str(n)
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False
    return True

def make_tidy(n, s, l):
    if len(s) > l:
        print('unexpected error!')
    elif len(s) == l:
        if int(s) > n:
            return -1
        if is_tidy(s):
            return int(s)

    for i in range(9, int(s[-1])-1, -1):
        x = make_tidy(n, s+str(i), l)
        if x != -1: return x
    return -1
    

rfile, wfile = None, None
if not TEST:
    fname = input().strip()

    rfile = open(''.join([fname, '.in']), 'r')
    wfile = open(''.join([fname,'.out']), 'w')

t = int(read(rfile))

for i in range(1, t + 1):
    n = int(read(rfile))
    if is_tidy(n):
        output = n
    else:
        l = ceil(log10(n))
        output = make_tidy(n, '0', l+1)
    write("Case #{}: {}".format(i, output), file=wfile)

if not TEST:
    rfile.close()
    wfile.close()
