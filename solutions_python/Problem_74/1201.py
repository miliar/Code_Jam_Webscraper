#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import optparse

OTAG = 'O'
BTAG = 'B'
BOTS = [OTAG, BTAG]

WAIT = 0
FORWARD = 1
BACK = -1
PUSH = 99
FINISH = -99

def algo(data):
    positions = {}
    sequences = {}
    states = {}

    for bot in BOTS:
        positions[bot] = 1
        sequences[bot] = getSeq(bot, data)
        states[bot] = 0

    time = 0
    while True:
        time += 1
        for bot in BOTS:
            states[bot] = doAction(bot, positions[bot], sequences[bot],  data)
            if states[bot] == FORWARD:
                positions[bot] += 1
            else:
                if states[bot] == BACK:
                    positions[bot] -= 1

        for bot in BOTS:
            if states[bot] == PUSH:
                next(sequences[bot])
                next(data)

        if states[OTAG] == FINISH and states[BTAG] == FINISH:
            return time - 1

def doAction(tag, pos, seq, data):
    # finish
    if len(data) == 0:
        return FINISH
    if len(seq) == 0:
        return FINISH

    # moving
    if pos != seq[0]:
        d = seq[0] - pos
        if d > 0:
            return FORWARD
        else: return BACK

    # not moving
    if tag + " " + str(pos) == data[0]:
        return PUSH
    else: return WAIT

def getSeq(tag, data):
    tmp = []
    for d in data:
        t, p = d.split(' ')
        if t == tag: tmp.append(int(p))
    return tmp

def shell(data):
    tokens = data.split(' ')
    k = int(next(tokens))

    tmp = []
    for t in range(k):
        if tokens[2*t] and tokens[2*t+1]:
            tmp.append(tokens[2*t] + ' ' + tokens[2*t+1])
    tokens = tmp


    return algo(tokens)

def next(data):
    data.reverse()
    tmp = data.pop()
    data.reverse()
    return tmp

def main(args):
    '''\
    %prog [options]
    '''
    case = 0
    for line in open(args[0]):
        line = line.decode('utf-8')
        line = line.strip()

        tokens = line.split(' ')
        if len(tokens) == 1:
            pass
        else :
            print 'Case #' + str(case) + ":", shell(line)
        case += 1

    return 0

if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))

