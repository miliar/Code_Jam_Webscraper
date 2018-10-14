#!/usr/bin/env python

import sys
from time import sleep


class Bot(object):
    def __init__(self, data, uid):
        self.done = False
        self.data = data
        self.uid = uid
        self.pos = 1
        self.n = None

    def run(self, canpress):
        if not self.n:
            self.find_next()
        if self.done:
            return
        if self.pos < self.n:
            self.pos += 1
        elif self.pos > self.n:
            self.pos -= 1
        elif self.pos == self.n:
            if self.data[0] == (self.uid, self.pos) and canpress:
                # print "%s --- Press" % self.uid
                del self.data[0]
                self.find_next()
                return True
        # print "%s -- P:%d N:%d" % (self.uid, self.pos, self.n)

    def find_next(self):
        for i in self.data:
            if i[0] == self.uid:
                self.n = i[1]
                return
        self.done = True


def case(line):
    data = line.split()[1:]
    data = [data[i:i+2] for i in range(0, len(data), 2)]
    data = [(bot, int(i)) for bot, i in data]

    time = 0
    O = Bot(data, 'O')
    B = Bot(data, 'B')
    while True:
        time += 1
        # print "-- %d ----" % time
        B.run(not O.run(True))
        if O.done and B.done:
            break
    return str(time)


if __name__ == "__main__":
    f = open(sys.argv[1])
    numcases = int(f.readline().strip())
    for i in range(numcases):
        print "Case #%d: %s" % (i + 1, case(f.readline().strip()))

