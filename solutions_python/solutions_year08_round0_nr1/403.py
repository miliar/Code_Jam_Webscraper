#!/usr/bin/python
numcases = input()
for casenum in range(numcases):
    numsearchengines = input()
    searchengines = []
    for i in range(numsearchengines):
        searchengines.append(raw_input())
    numqueries = input()
    switches=0
    found = {}
    for i in range(numqueries):
        query = raw_input()
        found[query] = 1
        if len(found.keys()) == numsearchengines:
            switches += 1
            found = {query: 1,}
    print ''.join(["Case #",str(casenum+1),": ",str(switches)])
