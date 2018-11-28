import os.path
import itertools

def fits(word, pattern):
    for w, p in itertools.izip(word, pattern):
        if w not in p:
            return False
    return True

def run_problem(dictionary, patterns):
    patterns = [list(pattern) for pattern in patterns]
    ret = [0] * len(patterns)
    for word in dictionary:
        c = 0
        for pattern in patterns:
            if fits(word, pattern):
                ret[c] += 1
            c += 1
    return ret

def write_output(outfile, output):
    out = open(outfile, 'w')
    i = 1
    for value in output:
        out.write('Case #%d: %d\n' % (i, value))
        i += 1
    out.close()

def parse_pattern(pattern):
    for first in pattern.split('('):
        halves = first.split(')')
        if len(halves) == 1:
            for letter in halves[0]:
                yield letter
        else:
            yield halves[0]
            for letter in halves[1]:
                yield letter

def test_pattern():
    patterns = ['(ab)(bc)(ca)', 'abc', '(abc)(abc)(abc)', '(zyx)bc']
    out = [['ab','bc','ca'], ['a','b','c'], ['abc','abc','abc'],['zyx','b','c']]
    for pattern, outtest in zip(patterns, out):
        assert(outtest == list(parse_pattern(pattern)))


def iterate_patterns(patterns):
    for pattern in patterns:
        yield parse_pattern(pattern)

def run(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    input.close()
    first = lines.pop(0).split()
    elle = int(first[0])
    dee  = int(first[1])
    enn  = int(first[2])
    d = [line.strip() for line in lines[:dee]]
    patterns = [line.strip() for line in lines[dee:dee+enn]]
    del lines
    write_output('out2',
            run_problem(d, iterate_patterns(patterns)))

if __name__ == '__main__':
    import sys
    run(sys.argv[1])
    #test_pattern()
