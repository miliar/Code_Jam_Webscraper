def solve():
  times = 0
  speed = 2
  C, F, X = map(float, raw_input().split())
  res = X / 2;
  while True:
    times += C / speed;
    speed += F;
    if(res < times + X / speed):
      break
    res = times + X / speed;
  return res
if __name__ == "__main__":
  tn = int(raw_input())
  for cn in range(tn):
    print 'Case #%d: %.7f' % (cn + 1, solve())
    