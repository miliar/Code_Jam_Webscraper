from itertools import count

def solveDataSet(R, k, groups):
    queue = groups
    revenue = 0
    for i in range(R):
        coaster = []
        while queue and queue[0]+sum(coaster) <= k:
            coaster.append(queue[0])
            revenue += queue[0]
            queue.pop(0)
        for group in coaster:
            queue.append(group)
    return revenue

input_file = file('C-small-attempt1.in', 'r')
t = input_file.next()
results = []
try:
    for i in count(1):
        R, k, N = (int(x) for x in input_file.next().split())
        groups = [int(x) for x in input_file.next().split()]
        results.append(solveDataSet(R, k, groups))
except StopIteration:
    input_file.close()

for i,r in enumerate(results):
    print "Case #%s: %s" % ((i+1), r)
