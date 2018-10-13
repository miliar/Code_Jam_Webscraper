wtc = 'welcome to code jam'
t1 = 'elcomew elcome to code jam'
t2 = 'wweellccoommee to code qps jam'
t3 = 'welcome to codejam'

# Naive recursive version
def howManyTimes(needle, haystack):
    if len(needle) == 1:
        return len([x for x in haystack if needle == x])
    else:
        if len(haystack) == 0:
            return 0
        else:
            head_needle = needle[0]
            tail_needle = needle[1:]
            head_haystack = haystack[0]
            tail_haystack = haystack[1:]
            if head_needle  == head_haystack:
                return howManyTimes(needle, tail_haystack) + \
                       howManyTimes(tail_needle, tail_haystack)
            else:
                return howManyTimes(needle, tail_haystack)

# Tabulated results version (for efficiency)
class HowManyTimes:
    def __init__(self, needle, haystack):
        self.n = needle
        self.h = haystack
        
        self.table = []
        for c in needle:
            self.table.append([None] * len(haystack))

    def get_count(self):
        return self.aux_gc(0, 0) 

    def aux_gc(self, ind_n, ind_h):
        if ind_h == len(self.h) or ind_n == len(self.n):
            return 0

        if self.table[ind_n][ind_h] != None:
            # table lookup
            return self.table[ind_n][ind_h]
        else:
            if ind_n == len(self.n) - 1:
                char = self.n[ind_n]
                val = len([x for x in self.h[ind_h:] if x == char])
            else:
                if self.n[ind_n] == self.h[ind_h]:
                    val = self.aux_gc(ind_n, ind_h + 1) + \
                          self.aux_gc(ind_n + 1, ind_h + 1)
                else:
                    val = self.aux_gc(ind_n, ind_h + 1)
                
            # store
            val = val % 10000
            self.table[ind_n][ind_h] = val
            return val

def parseInput(f):
    lines = open(f).readlines()
    num_lines = int(lines[0])
    strings = []
    for i in range(num_lines):
        strings.append(lines[1+i])
    return strings

#print howManyTimes(wtc, t2)
#print HowManyTimes(wtc, t2).get_count()

if __name__ == '__main__':
    i = 1
    for s in parseInput('input.txt'):
        print "Case #%s: %.4i" % (i, HowManyTimes(wtc, s).get_count())
        i = i + 1
