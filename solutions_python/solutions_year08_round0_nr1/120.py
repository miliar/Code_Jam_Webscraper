#!/bin/env python
# -*- coding: utf-8 -*-
'''Python for Google Code Jam 2008 Qualification Round, Saving The Universe

Problem

The urban legend goes that if you go to the Google homepage and search for
"Google", the universe will implode. We have a secret to share... It is true!
Please don't try it, or tell anyone. All right, maybe not. We are just kidding.

The same is not true for a universe far far away. In that universe, if you
search on any search engine for that search engine's name, the universe does
implode!

To combat this, people came up with an interesting solution. All queries are
pooled together. They are passed to a central system that decides which query
goes to which search engine. The central system sends a series of queries to one
search engine, and can switch to another at any time. It must never send a query
to a search engine whose name matches the query. In order to reduce costs, the
number of switches should be minimized.

Your task is to tell us how many times the central system will have to switch
between search engines, assuming that we program it optimally.

Input

The first line of the input file contains the number of cases, N. N test cases
follow.

Each case starts with the number S -- the number of search engines. The next S
lines each contain the name of a search engine. Each search engine name is no
more than one hundred characters long and contains only uppercase letters,
lowercase letters, spaces, and numbers. There will not be two search engines
with the same name.

The following line contains a number Q -- the number of incoming queries. The
next Q lines will each contain a query. Each query will be the name of a search
engine in the case.

Output

For each input case, you should output:

Case #X: Y

where X is the number of the test case and Y is the number of search engine
switches. Do not count the initial choice of a search engine as a switch.

Limits

0 < N ≤ 20

Small dataset

2 ≤ S ≤ 10

0 ≤ Q ≤ 100

Large dataset

2 ≤ S ≤ 100

0 ≤ Q ≤ 1000

Sample

Input
----
2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol

Output
----
Case #1: 1
Case #2: 0

In the first case, one possible solution is to start by using Dont Ask, and
switch to NSM after query number 8.
For the second case, you can use B9, and not need to make any switches.

'''

try: x = set()
except SyntaxError:
  print "Requires Python 2.4 or above (set needed)"
  import sys
  sys.exit(1)

def save_the_universe(inputs):
    '''Generate output for the 'Saving the Universe' problem

    Example:
    >>> i = """2
    ... 5
    ... Yeehaw
    ... NSM
    ... Dont Ask
    ... B9
    ... Googol
    ... 10
    ... Yeehaw
    ... Yeehaw
    ... Googol
    ... B9
    ... Googol
    ... NSM
    ... B9
    ... NSM
    ... Dont Ask
    ... Googol
    ... 5
    ... Yeehaw
    ... NSM
    ... Dont Ask
    ... B9
    ... Googol
    ... 7
    ... Googol
    ... Dont Ask
    ... NSM
    ... NSM
    ... Yeehaw
    ... Yeehaw
    ... Googol"""
    >>> print save_the_universe(i)
    Case #1: 1
    Case #2: 0
    '''
    line = inputs.split("\n")
    l = 0

    num_cases = int(line[l])
    l+=1
    solution = []
    
    for c in xrange(num_cases):
        num_engines = int(line[l])
        l+=1;
        engine = []
        for e in xrange(num_engines):
            engine.append(line[l])
            l+=1

        num_searches = int(line[l])
        l+=1
        search = []
        for s in xrange(num_searches):
            search.append(line[l])
            l+=1

        solution.append(solve(engine, search))

    output = []
    for s, n in zip(solution, xrange(1, num_cases+1)):
        output.append("Case #%d: %d"%(n ,s))
    return "\n".join(output)

def solve(engines, searches):
    '''Solve a 'Save the universe' problem

    Example:
    >>> engines = """
    ... Yeehaw
    ... NSM
    ... Dont Ask
    ... B9
    ... Googol""".split()
    >>> searches = """
    ... Yeehaw
    ... Yeehaw
    ... Googol
    ... B9
    ... Googol
    ... NSM
    ... B9
    ... NSM
    ... Dont Ask
    ... Googol""".split()
    >>> print solve(engines, searches)
    1
    >>> engines = """
    ... Yeehaw
    ... NSM
    ... Dont Ask
    ... B9
    ... Googol""".split()
    >>> searches = """
    ... Googol
    ... Dont Ask
    ... NSM
    ... NSM
    ... Yeehaw
    ... Yeehaw
    ... Googol""".split()
    >>> print solve(engines, searches)
    0
    '''
    engine_count = len(engines)
    engines_searched = set()
    switches = 0
    for search in searches:
        engines_searched.add(search)
        if len(engines_searched) == engine_count:
            switches += 1
            engines_searched = set([search])
    return switches

def _usage():
    print "Usage: saving_the_universe.py <input_file> <output_file>"
    print "If output_file omitted, printed to stdout"

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        _usage()
        print "Running test suite..."
        failed, total = _test()
        if (not failed): print "All %d tests passed"%total
    elif len(sys.argv) == 2:
        inputs = file(sys.argv[1]).read()
        print save_the_universe(inputs)
    elif len(sys.argv) == 3:
        inputs = file(sys.argv[1]).read()
        file(sys.argv[2],"w").write(save_the_universe(inputs))
    else:
        _usage()
        sys.exit(1)
