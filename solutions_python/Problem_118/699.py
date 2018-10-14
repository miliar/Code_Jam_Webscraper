import sys
from math import *

def gen_palind(a, b):
    pal = Palind(a)
    if pal.getValue() <= b:
        yield pal.getValue()
        while pal.increment() <= b:
            yield pal.getValue()

class Palind:
    def __init__(self, a):
        self.digits_len = len(str(a))
        self.high_digits = a / (10 ** (self.digits_len / 2 + self.digits_len % 2))
        while self.getValue() < a:
            self.increment()

    def increment(self):
        if (self.digits_len > 1 and str(self.high_digits)[0] == '3') or self.high_digits == 10 ** len(str(self.high_digits)) - 1:
            if self.digits_len % 2:
                self.high_digits = 10 ** (len(str(self.high_digits)) - 1)
            else:
                self.high_digits = 10 ** len(str(self.high_digits))
            self.digits_len += 1
        else:
            self.high_digits += 1
            #        print self.high_digits, self.digits_len, self.getValue()
        return self.getValue()

    def getValue(self):
        l = list( str(self.high_digits) )
        #        print l
        #print l[::-1]
        ret = l + l[::-1]
        if self.digits_len % 2:
            del ret[len(l)]
        return int("".join(ret))


def isPalind(a):
    s = str(a)
    for i in range(len(s) /2):
        if s[i] != s[len(s)-1 -i]:
            return False
    else:
        return True



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        A, B = [ int(e) for e in sys.stdin.readline().strip().split()]
        #        print A, B
        a = int(sqrt(A))
        if A != a*a:
            a += 1
        b = int(sqrt(B))
        #print a, b
        ret = 0
        for p in gen_palind(a, b):
            #            print p
            if isPalind(p*p):
                #                print p, p*p
                ret += 1
        print "Case #%d: %d" % (t+1, ret)
