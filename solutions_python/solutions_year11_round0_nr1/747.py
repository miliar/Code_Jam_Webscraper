#!/usr/bin/python

ORANGE = 1
BLUE = 2

def parse(data):
    cases = []
    for row in data: 
        elem = row.split(' ')[1:]

        case = []
        for i in range(0, len(elem), 2):
            case.append( (BLUE if elem[i]=='B' else ORANGE, int(elem[i+1])) )
        cases.append(case)
    return cases


def run(case):
    pos = [ -1, 1, 1 ]

    total = 0
    bot = case[0][0]
    group = 0

    for step in case:
        # calculate the steps needed to move
        #   offset of target bot from position + 1
        cost = abs(step[1] - pos[step[0]]) + 1

        # move bot
        pos[step[0]] = step[1]

        # adjust cost if there was prep time
        #   subtract the total amount from previous group
        if bot != step[0]:
            cost = cost - group
            cost = max(cost, 1)  # at least 1
            group = 0
            bot = step[0]

        # add cost to grouping and total
        group += cost
        total += cost

    return total


def output(n, result):
    return "Case #%d:  %d" % (n, result)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Pass filename"

    inp = sys.argv[1]
    outp,_ = inp.rsplit('.',1)
    outp += ".out"

    f = open(inp, 'r')
    data = [ l.strip() for l in f.readlines() ]
    data = data[1:]
    f.close()

    cases = parse(data)

    out = open(outp, 'w')
    for i,case in enumerate(cases):
        result = run(case)
        out.write( output(i+1, result) )
        out.write("\n")
    out.close()
