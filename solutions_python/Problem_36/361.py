#!/usr/bin/env python
import sys
import re
import time

class Banner(object):
    def __init__(self, file):
        self.cases = self.parse(file)
        self.phrase = 'welcome to code jam'


    def parse(self, file):
        fp = open(file)
        lines = fp.readlines()
        fp.close()
        info = lines.pop(0)

        cases = []
        for line in lines:
            cases.append(str(line))

        return cases

    def search_phrase(self, case):
        desl = [0 for i in self.phrase]
        count = 0
        i = 1
        desl[0] = case.find(self.phrase[0])

        while desl[0] != -1:
            while i < len(self.phrase):
                print len(case)
                for k in desl:
                    print k, ' ',
                print
                if desl[i] == 0 and i != 0:
                    desl[i] = case.find(self.phrase[i], desl[i-1]+1)
                else:
                    desl[i] = case.find(self.phrase[i], desl[i]+1)

                if desl[i] != -1:
                    i += 1
                elif i == 0:
                    break
                else:
                    desl[i] = 0
                    i -= 1

            else:
                count += 1
                i -= 1


        return count



    def run(self):
        output = open('output.txt', 'w')
        print len(self.cases)
        for case, i in zip(self.cases, range(len(self.cases))):
            match = self.search_phrase(case)
            match = match%10000

            out = 'Case #%d: %04d\n' % (i+1, match)
            output.write(out)
        output.close()

        return 0





def main(argv):
    if len(argv) != 2:
        sys.stderr.write("USE: %s <input file>" % argv[0])
        return 1

    banner = Banner(argv[1])
    banner.run()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
