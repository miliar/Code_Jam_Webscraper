# coding: utf-8

import re

class AlienLanguage(object):
    def __init__(self, input):
        lines = input.strip().splitlines()
        self.l, self.d, self.n = map(lambda s: int(s), lines[0].split())
        self.data = lines[1:self.d+1]
        self.testcases = []
        for testcase in lines[self.d+1:self.d+self.n+1]:
            self.testcases.append(re.compile(testcase.strip().replace('(','[').replace(')',']')))

    def test(self):
        case_number = 1
        for testcase in self.testcases:
            matched = 0
            for data in self.data:
                if testcase.match(data):
                    matched = matched + 1
            print("Case #%d: %d" % (case_number, matched))
            case_number += 1

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("[usage] %s [input file]" % sys.argv[0])
        sys.exit(0)

    input = None
    with open(sys.argv[1], 'r') as f:
        input = "".join(f.readlines())
    AlienLanguage(input).test()
