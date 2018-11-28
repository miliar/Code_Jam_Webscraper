import string, math
import heapq

#inputFile = open('large_input_test.in', 'r')
inputFile = open('B-small-attempt0.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
data      = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def computeAnswer(n,r,o,y,g,b,v):
    if (r+o+v) * 2 > n or (y+o+g) * 2 > n or (b+g+v) * 2 > n:
        return "IMPOSSIBLE"

    # Assuming no O, G, or V for now.
    
    solution = []
    heap = [(-r, "R"), (-y, "Y"), (-b, "B")]
    heapq.heapify(heap)

    prevPopped = heapq.heappop(heap)
    solution.append(prevPopped[1])
    prevPopped = (prevPopped[0] + .9, prevPopped[1])

    while len(heap) > 0:
        nextPopped = heapq.heappop(heap)
        if nextPopped[0] > -.5:
            break
        solution.append(nextPopped[1])
        heapq.heappush(heap, prevPopped)

        prevPopped = (nextPopped[0] + 1, nextPopped[1])
    
    return string.join(solution, "")


for case in xrange(1, numCases+1):
    n,r,o,y,g,b,v = map(int, data[case].split(" "))
    answer  = computeAnswer(n,r,o,y,g,b,v)

    print formatAnswer(case, answer)


