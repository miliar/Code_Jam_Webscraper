import heapq

testcases = open('B-large.in').read().strip().split('\n')
fout = open("output.txt","w")

N = int(testcases[0])
for i in range(N):
  nd = int(testcases[2*i+1])
  plates = [int(x) for x in testcases[2*i+2].split(' ')]
  plates.sort(reverse = True)

  tempplates = []
  for k in range(nd):
    tempplates.append([-plates[k], plates[k], 1])

  heapq.heapify(tempplates)
  best = -tempplates[0][0]
  idx = 0
  while idx < 1000 and tempplates[0][0] < -1:
    node = heapq.heappop(tempplates)
    node[2] += 1
    heapq.heappush(tempplates, [(node[1]+node[2]-1)/node[2]*-1, node[1], node[2]])
    idx += 1
    
    best = min(best, idx - tempplates[0][0])

  print >>fout, "Case #" + str(i+1) + ":", best

