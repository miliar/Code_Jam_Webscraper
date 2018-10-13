import random
import re
import sys

elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
available = filter(lambda x: x not in elements, map(chr, range(65,91)))

def write_large_test_case(filename):
    f = open(filename, 'w')
    for _ in range(100):
        f.write(generate_test_case(36, 28, 100)+'\n')
    f.close()

def write_small_test_case(filename):
    f = open(filename, 'w')
    for _ in range(100):
        f.write(generate_test_case(1, 1, 10)+'\n')
    f.close()

def generate_test_case(combinations, opposers, input_length):
    case = str(combinations) + ' '

    combs = {}
    combs_range = range(random.randint(0, combinations))
    for _ in combs_range:
        comb2 = comb1 = ''
        while comb2==comb1 or ''.join(sorted(comb1+comb2)) in combs:
            comb1 = random.choice(elements)
            comb2 = random.choice(elements)

        comb3 = random.choice(available)
        combs[''.join(sorted(comb1+comb2))] = comb3

    case += ' '.join([k+v for k,v in combs])

    oppos = []
    oppos_range = range(random.randint(0, opposers))
    for _ in oppos_range:
        oppo2 = oppo1 = ''
        while oppo2==oppo1 or ''.join(sorted(oppo1+oppo2)) in oppos:
            oppo1 = random.choice(elements)
            oppo2 = random.choice(elements)

        oppos.append(''.join(sorted(oppo1+oppo2)))

    case += str(opposers) + ' '
    case += ' '.join(oppos)

    case += ' '
    for _ in range(random.randint(1, input_length)):
        case += random.choice(elements)

    return case


def parse_test_case(line):
    line_data = line.split(' ')
    num_combinations = int(line_data[0])
    end_combinations = num_combinations+1
    combinations = {}
    if num_combinations:
        combinations = dict([(''.join(sorted(c[:2])), c[2]) for c in line_data[1:end_combinations]])

    num_opposers = int(line_data[end_combinations])
    end_opposers = end_combinations+num_opposers+1
    opposers = []
    if num_opposers:
        opposers = line_data[end_combinations+1:end_opposers]

    in_ = line_data[-1].strip()

    return combinations, opposers, in_

def run_test_case(combinations, opposers, line):
    opposers_match = '(%s)' % ('|'.join([('%s.*%s|%s.*%s') % (x[0], x[1], x[1], x[0]) for x in opposers]),)
    i = 2
    eol = len(line)
    #import pdb; pdb.set_trace()
    while i<=eol:
        if i>0:
            last_2_sorted = ''.join(sorted(line[i-2:i]))
            if last_2_sorted in combinations:
                line = line[:i-2] + combinations[last_2_sorted] + line[i:]
                eol = eol - 1

            if opposers and re.search(opposers_match, line[:i]):
                line = line[i:]
                i = 1
                eol = len(line)
        i+=1

    return line

if __name__=='__main__':
    f = open(sys.argv[1], 'r')
    num_test_cases = int(f.readline())
    for i in range(num_test_cases):
        test_case = parse_test_case(f.readline())
        print 'Case #%d: [%s]' % (i+1, ', '.join(list(run_test_case(*test_case))))
    f.close()