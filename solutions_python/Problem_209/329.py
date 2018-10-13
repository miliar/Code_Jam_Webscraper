import heapq
import math

def main():
  for t in xrange(int(raw_input())):
    (N, K) = (int(x) for x in raw_input().split())
    pancakes = []
    for n in xrange(N):
      (r, h) = (int(y) for y in raw_input().split())
      pancakes.append((r, h))
    pancakes.sort()

    currPancakes = [((r*h), r, h) for (r, h) in pancakes[:K]]
    heapq.heapify(currPancakes)
    summation = sum([2 * r * h for (r, h) in pancakes[:K]])
    (bR, bH) = pancakes[K-1]
    bottomArea = bR*bR

    pancakes = pancakes[K:]
    for (r, h) in pancakes:
      tempSum = summation - 2 * currPancakes[0][0] + 2 * r * h
      if tempSum + r*r > summation + bottomArea:
        summation = tempSum
        heapq.heappop(currPancakes)
        heapq.heappush(currPancakes, (r*h, r, h))
        bottomArea = r*r

    print "Case #{}: {}".format(t+1, (summation + bottomArea) * math.pi)

if __name__ == "__main__":
  main()
