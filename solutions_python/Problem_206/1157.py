import operator

T = int(input())

for t in range(1, T + 1):
  [D, N] = [int(s) for s in input().split(" ")]
  # speed = []
  # left = []
  time = []
  for i in range(N):
    [ki, si] = [int(s) for s in input().split(" ")]
    # speed.append(si)
    # left.append(D-ki)
    time.append((D-ki)/si)

  # min_index, min_value = min(enumerate(speed), key=operator.itemgetter(1))
  # road_left = left[min_index]
  # time_pass = road_left / min_value
  max_time = max(time)

  print("Case #{}: {:.6f}".format(t, D/max_time))