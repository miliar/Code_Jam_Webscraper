file_in = open('a2.in', 'r')
file_out = open('a.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  d, n = map(int, file_in.readline().split())
  max_time = 0

  for i in range(n):
    ki, mi = map(int, file_in.readline().split())
    time = float(d - ki) / mi
    if time > max_time:
      max_time = time

  ans = d / max_time

  file_out.write("Case #{}: {}\n".format(t, ans))