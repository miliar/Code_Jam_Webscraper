import sys, itertools
cases = int(sys.stdin.readline())
case = 0

DEBUG=False

def to_digits(number):
    return [int(n) for n in str(number)]

def to_number(digits):
    n = 0
    i10 = 1
    for i, d in enumerate(reversed(digits)):
        n += d * i10
        i10 *= 10
    return n

def rotated(x, l): # REF: http://mail.python.org/pipermail/tutor/2002-February/012177.html
    if l <= 1:
        yield x
    else:
        for y in range(l):
            yield x[y:] + x[:y]    

while case < cases:

    print("Case #%d:" % (case+1), end=" ")
    case += 1

    line = sys.stdin.readline().split()
    min_number, max_number = int(line[0]), int(line[1])
    l = len(to_digits(min_number))
    
    pairs = 0
    for number in range(min_number, max_number+1):
        unique = []
        for p in rotated(to_digits(number), l):
            n = to_number(p)
            if number <  n <= max_number and n not in unique:
                pairs += 1
                unique.append(n)

    print(pairs)
        

