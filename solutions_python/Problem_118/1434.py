import sys
from itertools import starmap, izip

class FairNumber(object):
    def __init__(self, value, even):
        self.even = even
        self.value = list(value)
    def mult(self, a, b):
        return int(a) * int (b)
    @property
    def complete(self):
        complete = self.value if self.even else self.value[:-1]
        return complete + self.value[::-1]
    def is_squarable(self):
        return all([sum(starmap(self.mult, izip(seq, seq[::-1]))) < 10 
                    for seq in [self.complete[:l+1] 
                                for l in range(len(self.complete))]])
    def get_square(self):
        start = ''.join(str(sum(starmap(self.mult, izip(seq, seq[::-1]))))
                        for seq in [self.complete[:l+1] 
                                    for l in range(len(self.complete))])
        end = start[::-1]
        return start[:-1] + end
    def inc(self, index = 0):
        self.value[len(self.value) - index - 1] = str((int(self.value[
            len(self.value) - index - 1]) + 1) % 10)
        for i in range(index):
            self.value[len(self.value) - index + i - 1] = '0'
    def inc_for_next(self, index = 0):
        #print ''.join(self.complete), index
        if index > len(self.value) - 1:
            index = 0
            if self.even:
                self.value = list('1' + '0' * len(self.value))
            else:
                self.value = list('1' + '0' * (len(self.value) - 1))
            self.even = not self.even
        else:
            self.inc(index)
        if self.is_squarable():
            #print 'squarable %s' % ''.join(self.complete)
            return
        else:
            self.inc_for_next(index + 1)

class FairAndSquareRange(object):
    def __init__(self, A, B):
        #print A, B
        self.A = A
        self.B = B
        self.sqA = '1' + '0' * ((len(self.A) - 1) / 4)
        #print ''.join(self.sqA)
    def count_fair_and_square(self):
        #print '==========================='
        total = 0
        number = FairNumber(self.sqA, ((len(self.A) + 1) / 2) % 2 == 0)
        #print number.even
        #print number.value
        if number.is_squarable() and self.valid_number(number):
            total += 1
            #print "preadding: %s, %s" % (''.join(number.complete), number.get_square())
        number.inc_for_next()
        while(self.is_too_low(number)):
            number.inc_for_next()
        #print '----------'
        while(self.valid_number(number)):
            total += 1
            #print "adding: %s, %s" % (''.join(number.complete), number.get_square())
            number.inc_for_next()
            #print '----------'
        return total
    def is_too_low(self, number):
        l = len(number.complete)
        sql = 2 * l - 1
        if sql < len(self.A):
            return True
        if sql == len(self.A):
            return number.get_square() < self.A
        return False
    def valid_number(self, number):
        l = len(number.complete)
        sql = 2 * l - 1
        if sql < len(self.A) or sql > len(self.B):
            return False
        valid = True
        if sql == len(self.A):
            valid = valid and number.get_square() >= self.A
        if sql == len(self.B):
            valid = valid and number.get_square() <= self.B
        return valid

def get_fair_and_square(infile):
    return FairAndSquareRange(*infile.readline().split())

filename = sys.argv[1]
with open(filename)as infile:
    with open('.'.join([filename.split('.')[0], 'out']), 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            f_and_s = get_fair_and_square(infile)
            solution = "Case #%d: %d\n" % (case + 1, f_and_s.count_fair_and_square())
            #print solution
            outfile.write(solution)
