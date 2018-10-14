from math import pi

file_in = open('A-large.in', 'r')
file_out = open('a.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  n, k = map(int, file_in.readline().split())
  pancakes = []

  for i in range(n):
    r, h = map(int, file_in.readline().split())
    pancakes.append([r, h])
  
  pancakes.sort(key=lambda p: p[1])
  pancakes.sort(key=lambda p: p[0])

  for p in pancakes:
    p[1] = 2 * pi * p[0] * p[1]
    p[0] = p[0] * p[0] * pi

  heights = []
  ans = 0
  for p in pancakes:
    if len(heights) == k - 1:
      area = p[0] + p[1] + sum(heights)
      if area > ans:
        ans = area

    heights.append(p[1])
    heights.sort()
    if len(heights) == k:
      heights.pop(0)

  file_out.write("Case #{0}: {1:.10f}\n".format(t, ans))