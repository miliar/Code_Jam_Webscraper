#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

class Dancing(object):
 
    T_MAX = 30

    def __init__(self):
        self.p_max = {}
        for t in xrange(0, self.T_MAX + 1):
            self.p_max[t] = [self._p_max(t, False), self._p_max(t, True)]

    def _p_max(self, t, surprise=False):
        if surprise:
            if t == 0: return 0
            elif t ==1: return 1
            elif t % 3 == 2: return (t - 2)/3 + 2
            elif t % 3 == 0: return (t - 3)/3 + 2
            elif t % 3 == 1: return (t - 4)/3 + 2
        else:
            if t % 3 == 0: return t/3
            else: return t/3 + 1

    def sol(self, N, S, p, T):
        T = sorted(T, reverse=True)
        count = 0
        for i in xrange(len(T)):
            t = T[i]
            if self.p_max[t][0] >= p: count += 1
            elif self.p_max[t][1] >= p and S > 0:
                count += 1
                S -= 1
        return count

def test_cases(input):
    fi = open(input, "r")
    T = int(fi.next())
    for i in xrange(1, T + 1):
        tokens = map(lambda token: int(token), fi.next().split())
        yield i, tokens[0], tokens[1], tokens[2], tokens[3:]
    fi.close()

def main(input, output):
    fo = open(output, "w")
    problem = Dancing()
    for i, N, S, p, t in test_cases(input):
        result = problem.sol(N, S, p, t)
        fo.write("Case #{0}: {1}\n".format(i, result)) 
    fo.close()
        
if __name__ == "__main__":
    # Parse command options
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options] param1 param2")    
    parser.add_option("-i", "--input", dest="input", help="Input file")
    parser.add_option("-o", "--output", dest="output", help="Output file")
    options, args = parser.parse_args()
    main(options.input, options.output)
