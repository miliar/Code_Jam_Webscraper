import sys
import logging

def saving_the_universe(engines, queries, level=0):
    visited = set()
    count = 0
    for q in queries:
        if q not in visited:
            visited.add(q)
        else:
            log.debug('')
            
        if len(visited) == len(engines):
            visited.clear()
            visited.add(q)
            count += 1
    return count


# log initialization
logging.basicConfig()
log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)

# open files
input = open(sys.argv[1], 'r')
output = open('saving_the_universe.out', 'w')

# read input
lines = input.readlines()

# N - number of cases
N = int(lines[0])
del lines[0]

for case in range(N):
    engines = []
    queries = []

    #S - the number of search engines
    S = int(lines[0])
    del lines[0]

    for engine in range(S):
        engines.append(lines[0].strip())
        del lines[0]

    #Q - the number of incoming queries
    Q = int(lines[0])
    del lines[0]

    for query in range(Q):
        queries.append(lines[0].strip())
        del lines[0]

    log.info('Case #' + str(case+1) + ': ' + str(saving_the_universe(engines, queries)) + '\n')
    output.write('Case #' + str(case+1) + ': ' + str(saving_the_universe(engines, queries)) + '\n')

input.close()
output.close()
