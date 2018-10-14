#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

class SpeakingInTongues(object):
 
    SAMPLES  = [
            ("ejp mysljylc kd kxveddknmc re jsicpdrysi",
             "our language is impossible to understand"),
            ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
             "there are twenty six factorial possibilities"),
            ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
             "so it is okay if you want to just give up")
        ]

    def __init__(self):
        self.map = {"z": "q", "q": "z"}
        for s1, s2 in self.SAMPLES:
            for i in xrange(len(s1)):
                if s1[i] in self.map:
                    assert(self.map[s1[i]] == s2[i])
                self.map[s1[i]] = s2[i]    

    def sol(self, text):
        return "".join(map(lambda c: self.map[c], text))

def test_cases(input):
    fi = open(input, "r")
    T = int(fi.next())
    for i in xrange(1, T + 1):
        yield i, fi.next().strip()
    fi.close()

def main(input, output):
    fo = open(output, "w")
    problem = SpeakingInTongues()
    for i, text in test_cases(input):
        result = problem.sol(text)
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
