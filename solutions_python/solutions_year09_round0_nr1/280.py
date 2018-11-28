import re
import itertools

def read_file(filename):
    f = open(filename)
    contents = f.read().splitlines()
    return contents

contents = read_file('A-large.in')
L, D, N = [int(x) for x in contents.pop(0).split()]

words = frozenset(contents[:D])
assert len(words) == D
cases = contents[D:]
assert len(cases) == N

RE = re.compile(r'(\w|\(\w+\))')
def get_count(case):
    letters = [x.translate(None, '()') for x in RE.findall(case)]
    new_re = ''
    for substring in letters:
        if len(substring) > 1:
            new_re += '(%s)' % '|'.join(substring)
        else:
            new_re += substring
    new_re = '^%s$' % new_re
    compiled = re.compile(new_re)
    counter = 0
    for word in words:
        if compiled.match(word):
            counter += 1
    return counter

for i, case in enumerate(cases):
    print 'Case #%d: %d' % (i + 1, get_count(case))
