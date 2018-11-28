import math

PI = math.pi

in_f = None

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def str(self):
    return '(%d;%d)' % (self.x, self.y)

class Square(object):
  def __init__(self, lower_left, upper_right):
    self.lower_left = lower_left
    self.upper_right = upper_right

  def str(self):
    return '(%s, %s)' % (self.lower_left.str(), self.upper_right.str())

  def Area(self):
    return (self.lower_left.x - self.upper_right.x) ** 2

class Circle:
  def __init__(self, r):
    self.r = r


def DoCase(n):
  params = in_f.readline().split()
  [f, R, t, r, g] = map(float, params)
  #print '\nf, R, t, r, g'
  #print f, R, t, r, g

  # Innermost
  inner_rad = R - t - f
  circle = Circle(inner_rad)
  squares = []

  d = g + 2 * r
  num_squares_x = int(math.ceil(inner_rad / d))

  for i in range(num_squares_x):
    for j in range(num_squares_x):
      ll_point = Point(i*d + r + f, j*d + r + f)
      ur_point = Point(i*d + r + g - f, j*d + r + g - f)
      square = Square(ll_point, ur_point)
      squares.append(square)

  full_filter = lambda(s): IsSquareInCircle(s, circle) == 2
  partial_filter = lambda(s): IsSquareInCircle(s, circle) == 1

  fully_in_squares = filter(full_filter, squares)
  partially_in_squares = filter(partial_filter, squares)

  #print len(squares), len(fully_in_squares), len(partially_in_squares)

  total_area = PI * (R **2) / 4
  safe_area = 0
  for s in fully_in_squares:
    safe_area += s.Area()

  for s in partially_in_squares:
    safe_area += CommonArea(s, circle)

  print 'Case #%d: %f' % (n, (1 - safe_area / total_area))

def CommonArea(square, circle):

  left = right = top = bottom = False
  ll = square.lower_left
  ur = square.upper_right

  left_top_pt = right_bot_pt = None
  pts = []

  # left side:
  y = FindYIntersect(ll.x, circle)
  if between(y, ll.y, ur.y):
    left = True
    left_top_pt = Point(ll.x, y)

  # bottom
  x = FindXIntersect(ll.y, circle)
  if between(x, ll.x, ur.x):
    bottom = True
    right_bot_pt = Point(x, ll.y)

  # right side
  if not bottom:
    y = FindYIntersect(ur.x, circle)
    if between(y, ll.y, ur.y):
      right = True
      right_bot_pt = Point(ur.x, y)

  # top
  if not left:
    x = FindXIntersect(ur.y, circle)
    if between(x, ll.x, ur.x):
      top = True
      left_top_pt = Point(x, ur.y)

  if not left_top_pt or not right_bot_pt:
    print 'OH CRAP'

    print '\n  ', top
    print left, right
    print '  ', bottom

  area = StraightLineApproxArea(square, left, bottom, top, right, left_top_pt, right_bot_pt)
  area += CircleSegmentArea(circle.r, left_top_pt, right_bot_pt)
  return area

def between(x, lower, upper):
  return x >= lower and x <= upper

def FindYIntersect(x, circle):
  #print 'test', circle.r, x
  y = math.sqrt(circle.r ** 2 - x ** 2)
  return y

def FindXIntersect(y, circle):
  x = math.sqrt(circle.r ** 2 - y ** 2)
  return x

def CircleSegmentArea(r, top_pt, bottom_pt):
  a1 = math.asin(top_pt.y / r)
  a2 = math.asin(bottom_pt.y / r)
  theta = a1 - a2
  #print 'theta = %f deg' % math.degrees(theta)
  area = r **2 * 0.5 * (theta - math.sin(theta))
  #print 'area =', area
  return area

def StraightLineApproxArea(square, left, bottom, top, right, left_top_pt, right_bot_pt):

  a = left_top_pt.y - square.lower_left.y
  b = right_bot_pt.x - square.lower_left.x
  c = square.upper_right.x - left_top_pt.x
  d = square.upper_right.y - right_bot_pt.y

  side =  square.upper_right.x - square.lower_left.x

  if left and bottom:
    # Triangle
    return 0.5 * a * b

  elif top and right:
    # Square minus triangle
    return square.Area() - (0.5 * c * d)

  elif left and right:
    # Trapezia
    return side * (a + side - d) * 0.5

  elif top and bottom:
    return side * (b + side - c) * 0.5

  else:
    print 'CRAP...'


# Return 0: no, 1: partially, 2: yes
def IsSquareInCircle(square, circle):
  if not IsPointInCircle(square.lower_left, circle):
    return 0

  if IsPointInCircle(square.upper_right, circle):
    return 2
  else:
    return 1


def IsPointInCircle(pt, circle):
  distance_from_0_sq = pt.x ** 2 + pt.y ** 2
  return distance_from_0_sq <= circle.r ** 2


def main():
  global in_f
  in_f = file('in.txt', 'r')
  ncases = int(in_f.readline())
  for c in range(ncases):
    DoCase(c + 1)

if __name__ == '__main__':
  main()
