#!/usr/bin/env python

import sys

# return number_of_queries, number_of_searchengines
def find_all_searchengines(queries, searchengines):
    found=set()
    n=0
    while n<len(queries) and len(found)<len(searchengines):
	found.add(queries[n])
	n+=1
    return n, len(found)

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    numsearchengines=int(inputfile.readline().strip())
    searchengines=[]
    for i in range(numsearchengines):
	searchengines.append(inputfile.readline().strip())
    numqueries=int(inputfile.readline().strip())
    queries=[]
    for i in range(numqueries):
	queries.append(inputfile.readline().strip())
    numswitches=0
    sent=0
    while sent<numqueries:
	n, m = find_all_searchengines(queries[sent:], searchengines)
	if m<numsearchengines:
	    break
	if n==1:
	    raise Exception("no progress")
	sent+=n-1
	if sent>=numqueries:
	    raise Exception("error")
	#print "use %s, send %d queries" % (queries[sent], n-1)
	numswitches+=1
    print "Case #%d: %d" % (case, numswitches)
