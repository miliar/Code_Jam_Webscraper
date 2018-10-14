def how_many(arr):
  summation = 0
  res = 0
  for i in range(len(arr)):
      if summation < i:
          res += (i-summation)
          summation = i
      summation += arr[i]
  return res

ncases = int(raw_input())
for i in range(ncases):
  input = [int(num) for num in raw_input().split(' ')[1]]
  print("Case #" + str(i+1) + ": " + str(how_many(input)))
