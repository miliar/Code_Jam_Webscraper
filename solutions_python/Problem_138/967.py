import sys

def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for i in range(nr_cases):
            nr_blocks = int(fp.readline())
            naomi = map(float, fp.readline().strip().split(' '))
            ken = map(float, fp.readline().strip().split(' '))
            cases.append([nr_blocks, naomi, ken])
    return cases

def war(naomi, ken):
    points = 0
    ken = sorted(ken)
    for val in naomi:
        idx = None
        for j, val_ken in enumerate(ken):
            if val_ken > val:
                idx = j
                break
        if idx is not None:
            ken.pop(idx)
        else:
            points += 1
            ken.pop(0)
    return points

def deceitful_war(naomi, ken):
    points = 0
    ken = sorted(ken, reverse=True)
    for i, val in enumerate(sorted(naomi)):
        if val > ken[-1]:
            points += 1
            ken.pop(-1)
        else:
            ken.pop(0)
    return points

def evaluate(cases):
    output = ''
    for i, case in enumerate(cases):
        print i, case
        points_dw = deceitful_war(case[1], case[2])
        points_w = war(case[1], case[2])
        output += "Case #%d: %d %d\n" % (i+1, points_dw, points_w)
    print output
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)
    output = evaluate(cases)

    with open(out, 'w') as fp:
        fp.write(output)