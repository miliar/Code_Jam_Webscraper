input = """
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
"""

input = open('B-large.in').read()

def parse_input(input):
    input = input.strip().split('\n')
    for j,row in enumerate(input[1:]):
        row = row.split(' ')
        row.reverse()
        num_test_cases = int(row.pop())
        test_cases = {}
        opposed = []
        for i in xrange(num_test_cases):
            c = row.pop()
            test_cases[c[:2]] = c[2]
            test_cases[c[:2][::-1]] = c[2]
        num_opposed = int(row.pop())
        for i in xrange(num_opposed):
            opposed.append(set(row.pop()))
        row.pop()
        elements = row.pop()
        solve(j+1, test_cases, opposed, elements)

def solve(case, test_cases, opposed, elements):
    final = []
    for e in elements:
        final.append(e)
        test = ''.join(final[-2:])
        fset = set(final)
        if test_cases.has_key(test):
            final = final[:-2]
            final.append(test_cases.get(test))
        elif any(o.issubset(fset) for o in opposed):
            final = []
    print 'Case #%d: %s' % (case,final)

parse_input(input)
