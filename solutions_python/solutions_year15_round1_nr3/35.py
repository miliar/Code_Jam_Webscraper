
import math

# Convex hull code taken from 
# http://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python
def genConvexHull(points):
  """Computes the convex hull of a set of 2D points.

  Input: an iterable sequence of (x, y) pairs representing the points.
  Output: a list of vertices of the convex hull in counter-clockwise order,
    starting from the vertex with the lexicographically smallest coordinates.
  Implements Andrew's monotone chain algorithm. O(n log n) complexity.
  """

  # Sort the points lexicographically (tuples are compared lexicographically).
  # Remove duplicates to detect the case we have just one unique point.
  #points = sorted(set(points))

  # Boring case: no points or a single point, possibly repeated multiple times.
  if len(points) <= 1:
      return points

  # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
  # Returns a positive value, if OAB makes a counter-clockwise turn,
  # negative for clockwise turn, and zero if the points are collinear.
  def cross(o, a, b):
      return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

  # Build lower hull 
  lower = []
  for p in points:
      while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
          lower.pop()
      lower.append(p)

  # Build upper hull
  upper = []
  for p in reversed(points):
      while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
          upper.pop()
      upper.append(p)

  # Concatenation of the lower and upper hulls gives the convex hull.
  # Last point of each list is omitted because it is repeated at the beginning of the other list. 
  return lower[:-1] + upper[:-1]

# Is c between a and b?
# This code taken from 
# http://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
def isBetween(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
    if abs(crossproduct) != 0 : return False   # (or != 0 if using integers)

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0 : return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba: return False

    return True

def onConvexHull(p, convexHull):
  L = len(convexHull)
  for i in range(L):
    if (isBetween(convexHull[i], convexHull[(i+1) % L], p)):
      return True
  return False

#f = open('C.in', 'r')
f = open('C-small-attempt2.in', 'r')
#f = open('B-large.in', 'r')
T = int(f.readline())
for testCase in range(1, T+1):
  N = int(f.readline())
  points = range(N)
  for i in range(N):
    (x, y) = map(int, f.readline().split())
    points[i] = (x, y)

  
  sortedPoints = sorted(points)

  #print "number of elements in visited is %d" % len(visited)
  #sortedPoints = points
  print "Case #%d:" % (testCase)
  for curSquirrel in range(N):
    queue = [sortedPoints]

    visited = set()
    visited.add(tuple(sortedPoints))

    while queue:
    # print "There are now %d elements in the queue" % len(queue)
      #print queue[0]
      curSet = queue.pop(0)
      convexHull = genConvexHull(curSet)
      if (onConvexHull(points[curSquirrel], convexHull)):
        print len(points) - len(curSet)
        break
      else:
        for i in range(len(curSet)):
          if ((curSet[i][0] == points[curSquirrel][0]) and (curSet[i][1] == points[curSquirrel][1])):
            continue
          
          #print "trying %d. curSet is" % (i)
          #print curSet
          temp = list(curSet)
          del temp[i]
          if (tuple(temp) in visited): 
            continue
          queue.append(temp)
          visited.add(tuple(temp))



  


