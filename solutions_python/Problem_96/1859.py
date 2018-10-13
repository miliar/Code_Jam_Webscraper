from sys import stdin

def get_judge_points(total):
  if not isinstance(total, int):
    total = int(total)
  i = int(total/3)
  remainder = total % 3
  points = [i, i, i]
  while remainder > 0:
    points[remainder] += 1
    remainder -= 1
  return points

def do_surprise(points):
  diff = max(points) - min(points)
  if min(points) > 0:
    if diff == 0:
      points[0] -= 1
      points[1] += 1
    elif diff == 1:
      number_of_max = len(filter(lambda x: x == max(points), points))
      if number_of_max == 2:
        points[points.index(max(points))] -= 1
        points[points.index(max(points))] += 1
        
  return points

t = 0
for line in stdin.readlines():
  t_in = 0
  y = 0
  if t == 0:
    t_in == int(line.rstrip())
  else:
    numbers = line.rstrip().split(' ')
    n, s, p = map(lambda x: int(x), numbers[0:3])
    scores = map(get_judge_points, numbers[3:])
    for score in scores:
      diff = max(score) - min(score)
      if max(score) < p and (diff >= 0) and (p - max(score) <= 1) and s > 0:
        do_surprise(score)
        s -= 1
      if max(score) >= p:
        y += 1
    
    print 'Case #%i: %i' % (t, y)
    
  t += 1