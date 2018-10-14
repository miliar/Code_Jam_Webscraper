import sys
import numpy as np

def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            line = fp.readline().strip()
            cases.append(map(float, line.split(' ')))
    return cases

def evaluate(cases):
    output = ''
    for i, case in enumerate(cases):
        cps = 2.0
        print case
        print "Costs = %f" % case[0]
        print "Boost = %f" % case[1]
        print "Goal = %f" % case[2]

        time = case[2] / cps
        print "base time", time
        if case[0] <= case[2]:
            farm_count = 1
            farm_time = 0.0
            while True:
                farm_time += case[0] / (2.0 + (farm_count - 1) * case[1])
                new_time = farm_time + case[2] / (2.0 + farm_count * case[1])
                # print new_time
                if new_time >= time:
                    break
                time = new_time
                farm_count += 1
            print "min time", time
        output += "Case #%d: %.7f\n" % (i+1, time)
    assert len(output.strip().split('\n')) == len(cases)
    print output
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)
    output = evaluate(cases)

    with open(out, 'w') as fp:
        fp.write(output)