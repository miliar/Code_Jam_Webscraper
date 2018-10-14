import math

def fair_squares(start, end):
    ret = []

    a = int(math.ceil(math.sqrt(float(start))))
    b = int(math.floor(math.sqrt(float(end))))

    for n in range(a, b + 1):
        if is_palindrome(n) and is_palindrome(n * n):
            ret.append(n)

    return len(ret)

def is_palindrome(n):
    s = str(n)
    return s[::-1] == s

f = open('C-small-attempt0.in', 'r')
o = open('C-small-attempt0.out', 'w')

T = int(f.readline().strip())

i = 1
for t in xrange(T):
    line = f.readline().strip().split(' ')
    start = line[0]
    end = line[1]
    o.write("Case #" + str(i) + ": " + str(fair_squares(start, end)) + "\n")
    i += 1
