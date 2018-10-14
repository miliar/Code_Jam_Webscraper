import bisect

t = int(input())
for i in range(1, t + 1):
  N, K = map(int, input().split(' '))

  j = 0

  max_value = 0
  min_value = 0

  arr = [N]
  h = {N: 1}

  while j < K and len(arr) > 0:
    current = arr.pop()
    max_value = current // 2
    if (current % 2 == 0):
      min_value = max_value - 1
    else:
      min_value = max_value
    j += h[current]

    if (min_value in h):
      h[min_value] += h[current]
    else:
      h[min_value] = h[current]
      bisect.insort_left(arr, min_value)

    if (max_value in h):
      h[max_value] += h[current]
    else:
      h[max_value] = h[current]
      bisect.insort_left(arr, max_value)
  print("Case #{}: {} {}".format(i, max_value, min_value))