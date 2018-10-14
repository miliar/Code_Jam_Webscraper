import math

def solve(num_pancakes, pancakes, order_size):
  max_area = 0.0
  for R, H in pancakes:
    copy = list(pancakes)
    copy.remove((R, H))
    if order_size == 1:
      choose = []
    else:
      choose = sorted(copy, key=lambda x: x[0]*x[1])[-order_size + 1:]
    area = math.pi * (R*R + 2.0*R*H + sum(map(lambda x: 2.0*x[0]*x[1], choose)))
    if area > max_area:
      max_area = area
  return max_area

if __name__ == '__main__':

  num_cases = int(raw_input())
  for case in range(num_cases):
    line = raw_input().split(' ')
    num_pancakes, order_size = int(line[0]), int(line[1])
    pancakes = [None] * num_pancakes
    for i in range(num_pancakes):
      line = raw_input().split(' ')
      pancakes[i] = (float(line[0]), float(line[1]))
    solution = solve(num_pancakes, pancakes, order_size)

    print 'Case #{}: {}'.format(case+1, solution)
