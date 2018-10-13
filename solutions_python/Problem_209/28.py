import math

def optimalSurfaceAreaWithFixedBottom(N, K, radii, heights, bottomIndex):
  sortedProducts = sorted([(radii[i] * heights[i], i) for i in xrange(N)])[::-1]
  included       = 1
  result         = radii[bottomIndex]**2 + 2 * radii[bottomIndex] * heights[bottomIndex]
  sortedIndex = 0
  while included < K and sortedIndex < N:
    index = sortedProducts[sortedIndex][1]
    if index != bottomIndex and radii[index] <= radii[bottomIndex]:
      result   += 2 * radii[index] * heights[index]
      included += 1
    sortedIndex += 1
  if included < K:
    return 0
  return math.pi * result

def optimalSurfaceArea(N, K, radii, heights):
  best = 0
  for bottomIndex in xrange(N):
    best = max(best, optimalSurfaceAreaWithFixedBottom(N, K, radii, heights, bottomIndex))
  return best

with open('../inputs/A-large.in') as infile:
  with open('../outputs/A-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [N, K]  = map(int, infile.readline().split(' '))
      radii   = []
      heights = []
      for _ in xrange(N):
        [R, H] = map(int, infile.readline().split(' '))
        radii.append(R)
        heights.append(H)
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write('%.9f' % optimalSurfaceArea(N, K, radii, heights))
      outfile.write('\n')
