def cookie_clicker(tokens):
  token = iter(tokens)
  cases = int(next(token))
  for case in range(cases):
    time = 0.0
    speed = 2.0
    farm = float(next(token))
    newspeed = float(next(token))
    goal = float(next(token))
    while farm/speed + goal/(speed+newspeed) < goal/speed:
      time += farm/speed
      speed += newspeed
    yield case+1, time + goal/speed

if __name__ == "__main__":
  import sys
  for case, result in cookie_clicker(sys.stdin.read().split()):
    print("Case #%s: %f7" % (case, result))
