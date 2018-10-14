#!/usr/local/bin/pypy
import sys
import re

import codejam

prob = codejam.Problem()

# Program.

def answer(combinations, opposing, invoked):
    # The next few lines are evaluated only once per test case (100 times...)
    opposingregs = [re.compile('(.*%(a)s.*%(b)s|.*%(b)s.*%(a)s)' %
        {'a': l[0], 'b': l[1]}) for l in opposing]
    
    combinations = dict([(x[0:2], x[2]) for x in combinations] + [(x[0:2][::-1], x[2]) for x in combinations])
    
    output = ''
    last = ''
    for i in xrange(len(invoked)):
        output += invoked[i]
        combo = combinations.get(output[-2:])
        if not combo is None: output = output[:-2] + combo
        delete = any([r.match(output) for r in opposingregs])
        if delete: output = ''
    return str(list(output)).replace("'", '')

def emptyfalse(x): return x != ''

l = 0
for line in prob.readlines()[1:]:
    l += 1
    line = [x.strip() for x in re.split('\d+', line)[1:]]
    if len(line) != 3: raise BaseException(l)
    prob.write_case(answer(filter(emptyfalse, line[0].split(' ')),
        filter(emptyfalse, line[1].split(' ')),
        line[2]
    ))