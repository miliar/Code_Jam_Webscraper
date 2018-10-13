t = int(input())
for i in range(1, t + 1):
  N, K = [int(x) for x in input().split(' ')]
  pancakes = []
  for j in range(N):
    r, h = [float(x) for x in input().split(' ')]
    pancakes.append({'R':r, 'H': h, 'A': 2 * r * h})
  max = 0.0
  for j in range(N):
    p = pancakes[j]
    p2 = pancakes[:j]+pancakes[j+1:]
    area = p['R'] * p['R']
    area += p['A']
    p2.sort(key=lambda x: -x['A'])
    for k in range(K-1):
      area += p2[k]['A']
    if area > max:
      max = area
  max *= 3.14159265359
  print("Case #{}: {}".format(i, max))


