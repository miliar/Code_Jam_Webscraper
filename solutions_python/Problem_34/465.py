import re

def solve_case(words, pattern):
    r = pattern.replace('(', '[').replace(')', ']')
    r = re.compile(r'%s$' % r)
    
    i = 0
    for word in words:
        if r.match(word):
            i += 1
    return i

if __name__ == '__main__':
    import sys
    lines = [l.strip() for l in open(sys.argv[1])]
    l, d, n = [int(x) for x in lines[0].split()]
    lines = lines[1:]
    
    dictionary = lines[0:d]
    cases = lines[d:]
    
    assert len(cases) == n
    
    solved = [solve_case(dictionary, case) for case in cases]
    for i, solution in enumerate(solved):
        print 'Case #%i: %i' % (i + 1, solution)
