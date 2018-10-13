infile = "B-large.in.txt"
outfile = "B-large.out"
cases = []


def whl(cost, inc, target):
    time = 0
    rate = 2
    if target/2 <= (target+cost)/(rate+inc):
        return target/2
    while target / rate > (target + cost) / (rate + inc):
        # print target / rate, cost / rate
        time += cost / rate
        rate += inc
    return time + target / (rate - inc) - cost / (rate - inc)


def process(case):
    c, f, x = case
    result = whl(c, f, x)
    return "{0:.7f}".format(result)


def parse(lines):
    ''' take one or more lines and parse to a specific case'''
    k = 1
    while k < len(lines):
        case = map(float, lines[k].split())
        cases.append(case)
        k += 1


fin = open(infile, "r")
parse(fin.readlines())
fin.close()

fout = open(outfile, "w")

for i, c in enumerate(cases):
    fout.write('Case #{0}: {1}\n'.format(i + 1, process(c)))
    # print 'Case #{0}: {1}'.format(i + 1, process(c))
fout.close()
