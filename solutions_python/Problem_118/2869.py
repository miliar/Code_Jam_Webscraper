lines = filter(None, [line.rstrip('\n') for line in open('C-small-attempt0.in')])

casen = int(lines[0])
cases = []

def chunks(l, n):
    return (l[i:i+n] for i in xrange(0, len(l), n))

for i in chunks(lines[1:], 3):
    for x in i:
        cases.append(x.split())

def palindrome(n):
    return str(n) == str(n)[::-1]

def sqrt(n):
    i = 0
    while i*i < n:
        i += 1
    if i*i != n:
        return False
    else:
        return i

def find_fs(s, e):
    c = 0
    for i in xrange(s, e+1):
        if palindrome(i) and sqrt(i):
            if palindrome(sqrt(i)):
                c += 1
    return c

for x, y in enumerate(cases):
    print "Case #{0}: {1}".format(x + 1, find_fs(int(y[0]), int(y[1])))
