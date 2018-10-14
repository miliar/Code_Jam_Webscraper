
for case in range(1, int(input()) + 1):

  btns = input().split()
  N = int(btns.pop(0))

  robots, t = {}, 0
  for _ in range(N):
    r, btn = btns.pop(0), int(btns.pop(0))
    pos, time = robots.get(r, (1, 0))

    t += max(0, abs(pos - btn) - (t - time)) + 1
    robots[r] = (btn, t)

  print('Case #%d: %d' % (case, t))
