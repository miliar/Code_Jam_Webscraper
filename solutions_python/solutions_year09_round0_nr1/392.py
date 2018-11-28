#!/usr/bin/env python
import sys
import re

class Decipher(object):
    def __init__(self, file):
        self.alien_words, self.cases = self.parse(file)


    def parse(self, file):
        fp = open(file)
        lines = fp.readlines()
        fp.close()
        info = lines.pop(0)
        info = info.split(' ')
        alien_words = []

        for i in range(int(info[1])):
            alien_words.append(lines.pop(0))

        cases = []
        for line in lines:
            cases.append(str(line))

        return alien_words, cases

    def run(self):
        output = open('output.txt', 'w')
        for case, i in zip(self.cases, range(len(self.cases))):
            pattern = re.compile(case.replace('(', '[').replace(')', ']'))
            match = 0
            for word in self.alien_words:
                if pattern.match(word):
                    match += 1

            out = 'Case #' + str(i+1) + ': ' + str(match) + '\n'
            output.write(out)
        output.close()

        return 0





def main(argv):
    if len(argv) != 2:
        sys.stderr.write("USE: %s <input file>" % argv[0])
        return 1

    decipher = Decipher(argv[1])
    decipher.run()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
