__author__ = 'israel.roth@gmail.com'


## {{{ http://code.activestate.com/recipes/577821/ (r1)
def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
## end of http://code.activestate.com/recipes/577821/ }}}


def is_palyndrom(i):
    istr = str(i)
    rstr = istr[::-1]
    return istr == rstr


def count_fair_and_square(a, b):
    num_fair_and_square = 0
    start = isqrt(a)
    finish = isqrt(b)
    s = start
    while s <= finish:
        if is_palyndrom(s):
            fsq = s * s
            if (fsq >= a) and (fsq <= b):
                if is_palyndrom(fsq):
                    num_fair_and_square += 1
        s += 1
    return num_fair_and_square

# ok, get test cases...

testfile = open ('FairAndSquare.in')
line = testfile.readline()
ntests = int(line)

outfile = open('FairAndSquare.out', 'w')

for testnum in range(0,ntests):
    interval = testfile.readline()[:-1].split()
    a = long(interval[0])
    b = long(interval[1])
    result = count_fair_and_square(a, b)
    outfile.write ("Case #"+str(testnum+1)+": " + str(result) + "\n")

