#!/usr/bin/python
import sys

def solve(servers,queries):
#     print servers
#     print
#     print queries
#     print
#     print
#     print
    # Return the number of switches
    counter = 0
    while True:
        lastAppearance = {}
        for i in range(0,len(queries)):
            if queries[i] not in queries[i+1:]:
                lastAppearance[queries[i]] = i
        if len(lastAppearance) < len(servers):
            break
        else:
            minimum = lastAppearance[lastAppearance.keys()[0]]
            for server in lastAppearance.keys():
                if lastAppearance[server] < minimum:
                    minimum = lastAppearance[server]
            queries = queries[:minimum+1]
            counter = 1 + counter
    return counter

next = sys.stdin.readline
numberOfCases = int(next())
for caseNumber in range(1,numberOfCases+1):
    # Process a case
    numberOfServers = int(next())
    servers = []
    for a in range(1,numberOfServers+1):
        servers.append(next()[:-1])

    numberOfQueries = int(next())
    queries = []
    for a in range(1,numberOfQueries+1):
        queries.append(next()[:-1])
        
    print "Case #" + str(caseNumber) + ": " + str(solve(servers,queries))
