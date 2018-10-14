#!/usr/bin/python2
import sys
########################################################
# Sorry, it has *really* become a hack job.
# I blame alcohol and a deadline getting rather close...
########################################################

BOTS = ['B', 'O']

class Bot:
    def __init__(self, name):
        self.name = name
        self.index = 1
        self.steps = 0
        self._last = 0

    def __str__(self):
        return 'Bot %s' % self.name

    def to(self, to):
        req = abs(self.index - to) + 1
        self.index = to
        return req

    def last(self):
        return self._last

def solve(num, data):
    bots = [Bot('B'), Bot('O')]

    steps = int(data.pop(0))
    time = 0

    for i in xrange(steps):
        idx = BOTS.index(data.pop(0))
        bot = bots[idx]
        otherbot = bots[(idx + 1) % 2]

        button = int(data.pop(0))

        req = bot.to(button)
        last = otherbot.last()
        otherbot._last = 0
        actual = max(1, req - last)
        bot._last += actual
        time += actual

    print 'Case #%d: %d' % (num, time)

if len(sys.argv) < 2:
    print 'Usage: %s <input file>' % sys.argv[0]
    sys.exit(1)

fp = open(sys.argv[1])
cases = int(fp.readline())

i = 1

for line in fp:
    solve(i, line.split())
    i += 1
