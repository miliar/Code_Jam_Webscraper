#!/usr/bin/env python2.5

def solve_case(engines, queries):
    """
    Problem

    The urban legend goes that if you go to the Google homepage and search for
    "Google", the universe will implode. We have a secret to share... It is
    true! Please don't try it, or tell anyone. All right, maybe not. We are
    just kidding.

    The same is not true for a universe far far away. In that universe, if you
    search on any search engine for that search engine's name, the universe
    does implode!

    To combat this, people came up with an interesting solution. All queries
    are pooled together. They are passed to a central system that decides which
    query goes to which search engine. The central system sends a series of
    queries to one search engine, and can switch to another at any time.
    Queries must be processed in the order they're received. The central system
    must never send a query to a search engine whose name matches the query. In
    order to reduce costs, the number of switches should be minimized.

    Your task is to tell us how many times the central system will have to
    switch between search engines, assuming that we program it optimally.
    """
    # Solution: dynamic programming: starting from the end, know how many
    # switches we need if we start with each possible engine.  We could start
    # from the beginning since the problem is symmetric in time - but it's
    # easier to understand if we start from the end.
    switches = dict((e, 0) for e in engines)
    for q in reversed(queries):
        # We only have to switch if we start from `q`.
        # Other values don't need to be updated.
        switches[q] = min(switches[q2] + 1 for q2 in engines if q2 != q)
    return min(switches.values())

def main(lines):
    """
    Input

    The first line of the input file contains the number of cases, N. N test
    cases follow.

    Each case starts with the number S -- the number of search engines. The
    next S lines each contain the name of a search engine. Each search engine
    name is no more than one hundred characters long and contains only
    uppercase letters, lowercase letters, spaces, and numbers. There will not
    be two search engines with the same name.

    The following line contains a number Q -- the number of incoming queries.
    The next Q lines will each contain a query. Each query will be the name of
    a search engine in the case.

    Output

    For each input case, you should output:

    Case #X: Y

    where X is the number of the test case and Y is the number of search engine
    switches. Do not count the initial choice of a search engine as a switch.
    """
    lines = (line.strip() for line in lines)

    N = int(lines.next())
    for case in range(1, N + 1):
        S = int(lines.next())
        engines = [lines.next().strip() for i in range(S)]
        Q = int(lines.next())
        queries = [lines.next().strip() for i in range(Q)]
        print "Case #%s: %s" % (case, solve_case(engines, queries))

if __name__ == '__main__':
    import fileinput
    main(fileinput.input())
