import re
import sys

class CodeJammer(object):
    
    def __init__(self, fname):
        self.fp = open(fname, 'r', 4096)
        self.ch = self.fp.read(1)
        self.oncase = 1

    def skip_whitespace(self):
        while self.ch.isspace():
            self.ch = self.fp.read(1)

    def next_int(self):
        result = []
        self.skip_whitespace()
        while self.ch.isdigit():
            result.append(self.ch)
            self.ch = self.fp.read(1)
        return int(''.join(result))

    def execute(self):
        cases = self.next_int()

        for x in range(cases):
            self.finish_case(self.case())

    def finish_case(self, out):
        sys.stdout.write("Case #%d: %s\n" % (self.oncase, out))
        sys.stdout.flush()
        self.oncase += 1
