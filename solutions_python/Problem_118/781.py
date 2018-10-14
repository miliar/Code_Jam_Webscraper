import math

def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())

def test(n):
    s = str(n)
    if s != s[::-1]:
        return False
    s = str(n*n)
    return s == s[::-1]

def solve():
    A, B = readlinearray()
    return len(filter(test, range(int(math.ceil(math.sqrt(A))), int(math.floor(math.sqrt(B)) + 1))))

case_number = readint()
for case in xrange(case_number):
    print "Case #%s: %d" % (case + 1, solve())
