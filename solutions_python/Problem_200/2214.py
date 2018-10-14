from collections import namedtuple

Test = namedtuple('Test', 'N')

def read(line):
    return Test(int(line))

def findi(strn):
    return next((i for i in range(1, len(strn)) if strn[i-1] > strn[i]), 0)
    
def solve(test):
    strn = str(test.N)
    i = findi(strn)
    if not i:
        return strn
    else:
        prefix = str(int(strn[:i]) - 1)
        suffix = '9' * len(strn[i:])
        updated = prefix + suffix
        return int(updated) if not findi(updated) else solve(read(updated))

if __name__ == '__main__':
    infile = 'B-large.in'

    with open(infile) as src:
        lines = list(src.readlines())

    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
