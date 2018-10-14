t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  str, k = input().split(" ")  # read a list of integers, 2 in this case

  result = 0

  arr = []
  k = int(k)
  for c in str:
    if c == '+':
      arr.append(1)
    else:
      arr.append(0)

  j = 0
  N = len(arr)
  while j < N:
    if arr[j] == 0:
      result += 1

      if j + k > N:
        result = 'IMPOSSIBLE'
        break

      for x in range(j, j + k):
        arr[x] = (arr[x] + 1) % 2

    j += 1

  print("Case #{}: {}".format(i, result))