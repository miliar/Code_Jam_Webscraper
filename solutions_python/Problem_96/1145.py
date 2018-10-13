import sys
rl = lambda : sys.stdin.readline()

def solve(case):
  line_in = rl().strip().split(' ')
  n = int(line_in.pop(0))
  s = int(line_in.pop(0))
  p = int(line_in.pop(0))
  line_in = [int(goog) for goog in line_in]
  
  count = 0
  for googler in line_in:
    if googler / 3 >= p:
      count += 1
    elif googler % 3 == 0:
      k = googler / 3
      if s > 0 and (k+1) >= p and (k-1) >= 0:
        count += 1
        s -= 1
    elif googler % 3 == 1:
      k = (googler - 1) / 3
      if (k+1) >= p and (k+1) <= 10:
        count += 1
    elif googler % 3 == 2:
      k = (googler - 2) / 3
      if (k+1) >= p and (k+1) <= 10:
        count += 1
      elif s > 0 and (k+2) >= p and (k+2) <= 10:
        count += 1
        s -= 1
  print('Case #' + str(case) + ": " + str(count))

num_cases = int(rl())

for i in range(1, num_cases + 1, 1):
  solve(i)
