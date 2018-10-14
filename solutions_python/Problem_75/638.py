import sys, itertools, re

def get_input():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    data = []
    for line in lines[1:]:
        tokens =  map(lambda x: x.strip(), re.split('\d+', line))[1:]
        data.append(tokens)
    return data

def solve(case):
    combs, oppos, invokes = case
    combs = dict([(tuple(sorted(x[:2])), x[2]) for x in combs.split()])
    oppos = set(map(lambda x: tuple(sorted(x)), oppos.split()))
    invokes = list(invokes)

    # print "======="
    # print combs
    # print oppos
    # print invokes

    wsp = []
    for x in invokes:
        if wsp and combs.has_key(tuple(sorted([x, wsp[len(wsp)-1]]))):
            tail = wsp.pop()
            new_x = combs[tuple(sorted([x, tail]))]
            wsp.append(new_x)
        elif set(map(lambda t: tuple(sorted([x, t])), wsp)) & oppos:
            wsp = []
        else:
            wsp.append(x)
    return wsp

data = get_input()
# print data

for idx, case in enumerate(data):
    print ("Case #%s: %s" % (idx+1, solve(case))).replace("'", '')
