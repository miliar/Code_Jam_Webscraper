"""

"""

#import psyco; psyco.full()
#import pyximport; pyximport.install()

def gcd(x, y):
    while x != 0:
        x, y = y % x, x
    return y

dynamic = False
def solve(case, case_nb=None):
    N, PD, PG = case
    if N < 100 / gcd(100, PD):
        return 'Broken'
    if PD > 0 and PG == 0:
        return 'Broken'
    if PD < 100 and PG == 100:
        return 'Broken'
    return 'Possible'

def parse_input(dynamic=False):
    from sys import argv, stdin
    def try_int(s):
        try:
            return int(s)
        except:
            return s
    if len(argv) > 1:
        f = open(argv[1])
    else:
        f = stdin
    lines = f.read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:]
    # Number of lines per case
    if not dynamic:
        p = len(lines) / nb_inputs
    line_nb = 0
    for i in range(nb_inputs):
        if dynamic:
            line = map(try_int, lines[line_nb].split(' '))
            p = sum(line)
            if len(line) > 1:
                p += 1
            else:
                # I do not take a line that contain only the number of lines
                line_nb += 1
        case_lines = lines[line_nb:line_nb+p]
        case = [map(try_int, line.split(' ')) for line in case_lines]
        if not dynamic and p == 1:
            case = case[0]
        line_nb += p
        yield case

if __name__ == '__main__':
    for i, case in enumerate(parse_input(dynamic=dynamic)):
        case_nb = 'Case #%i: ' % (i+1)
        result = solve(case, i+1)
        if type(result) is list:
            result = ' '.join(map(str, result))
        elif type(result) is float:
            result = '%.06f' % result
        else:
            result = str(result)
        print case_nb + result
