import sys

def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        for line in fp:
            cases.append(map(int, line.split(' ')))
    assert nr_cases == len(cases)
    return cases

def run(cases):
    output = ''
    print cases
    for k, case in enumerate(cases):
        count = 0
        for i in range(case[0]):
            for j in range(case[1]):
                # print i,j, i&j
                if i&j < case[2]:
                    count += 1
        output += "Case #%d: %d\n" % (k+1, count)
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)

    output = run(cases)

    with open(out, 'w') as fp:
        fp.write(output)