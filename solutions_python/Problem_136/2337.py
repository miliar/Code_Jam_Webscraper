N = int(input())
for i in range(N):
  C, F, X = map(float, input().split())

  speed = 2
  time = 0
  x = 0
  while time + C / speed + X / (speed + F) < time + X / speed:
    time += C / speed
    speed += F
    x += 1
  print("Case #{0}: {1}".format(i + 1, time + X / speed))
