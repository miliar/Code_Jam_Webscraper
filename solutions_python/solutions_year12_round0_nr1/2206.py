from pprint import pprint
from difflib import Differ
from itertools import tee
import logging
import multiprocessing

__author__ = 'Robert'

class brain():
    def __init__(self, data):
        self.data = data
        self.cases = int(next(self.data))
        #self.N,self.M = map(int, data.next().split())
        #self.cache = {}
        self.results = list(self.solve_cases())

    def solve_cases(self):
        for case in range(1, self.cases + 1):
            result = self.solve_case(case)
            print result
            yield result

    def solve_case(self,case):
        x = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

        res = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

        d = dict(zip(x,res))
        d['q'] = 'z'
        d['z'] = 'q'
        print d
        #next(self.data)
        #line = next(self.data).split()
        #print line
        #v1 = map(int, next(self.data).split())
        #v2 = map(int, next(self.data).split())
        line = next(self.data)

        result = "".join(d[c] for c in line)

        return "Case #%s: %s" % (case, result)

def get_data(filename):
    try:
        with open(filename) as input_file:
            for line in input_file:
                line = line.strip()
                if line == "":
                    raise RuntimeError("blank line")
                yield line
    except IOError,e:
        print e
        for line in input_:
            yield line

def main():
    my_brain = brain(get_data("A-small-attempt0.in"))

    print ""
    print "checking results.. "
    pprint(list(Differ().compare(my_brain.results, solution)))

    #write results
    with open("out.txt",'w') as file_:
        file_.write("\n".join(my_brain.results))


table = """3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""
table = table.splitlines()
i = table.index("")
input_ = table[:i]
solution = table[i+1:]

if __name__ == '__main__':
    print ""
    print "running.."
    main()