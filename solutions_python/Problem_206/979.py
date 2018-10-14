def time_to_finish(pos, speed, dest):
  return (dest - pos) / speed

def solve(horses, dest):
  max_t = 0.0
  for pos, speed in horses:
    t = time_to_finish(pos, speed, dest)
    if t > max_t:
      max_t = t
  return dest / max_t

if __name__ == '__main__':

  num_cases = int(raw_input())
  for case in range(num_cases):
    line = raw_input().split(' ')
    dest, num_horses = float(line[0]), int(line[1])
    horses = []
    for _ in range(num_horses):
      line = raw_input().split(' ')
      position, speed = float(line[0]), float(line[1])
      horses.append((position, speed))
    solution = solve(horses, dest)

    print 'Case #{}: {}'.format(case+1, solution)
