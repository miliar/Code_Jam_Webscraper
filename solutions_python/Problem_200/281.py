def check(arr):
  index = -1
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      index = i
      break
  if index == -1: return False

  arr[i] = arr[i] - 1
  for i in range(i + 1, len(arr)): arr[i] = 9
  return True

_ = int(input())
for __ in range(1, _ + 1):
  arr = [int(ch) for ch in input()]
  while check(arr): pass
  print('Case #' + str(__) + ': ' + str(int(''.join(str(i) for i in arr))))
