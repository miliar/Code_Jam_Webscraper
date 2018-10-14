def countbluar(string):
    assert string

    count = 0
    out = []
    prev = ''
    for c in string:
        count += 1
        if c != prev and prev != '':
            out.append((prev, count-1))
            count = 1
        prev = c
    out.append((prev, count))
    return out

numCases = input()
for caseNum in xrange(numCases):
    strings = [ countbluar(raw_input()) for i in xrange(input()) ]
    # print strings
    length = len(strings[0])
    out = 'WTF!'

    def f(ret, a,b):
        print 'a', ret, a,b
        return ret

    # print zip(*strings)
    # print all([ len(s)==length for s in strings ])
    # print all([ reduce(lambda a,b: a if a[0]==b[0] else False, tuples)  for tuples in zip(*strings) ])
    # print

    if ( # all same length and all same characters at each posistion
        all([ len(s)==length for s in strings ]) and
        all([ reduce(lambda a,b: a if a[0]==b[0] else False, tuples)  for tuples in zip(*strings) ])
    ):
        out = 0
        for tupleslist in zip(*strings):
            counts = [ count for char, count in tupleslist]
            changes = min((
                    sum(( abs(count-target) for count in counts ))
                for target in xrange(min(counts), max(counts)+1)
            ))
            # print counts, changes
            out += changes

    else:
        out = 'Fegla Won'
    print 'Case #{0}: {1}'.format(caseNum+1, out)
