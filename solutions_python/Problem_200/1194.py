t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  digits = [int(x) for x in input()]
  pos = -1
  for j in range(len(digits)-1):
    if digits[j] > digits[j+1]:
      pos = j
      break
  if pos > -1:
    for j in range(pos+1, len(digits)):
      digits[j] = 9
    digits[pos] = digits[pos] - 1
    while pos > 0 and digits[pos-1] > digits[pos]:
      digits[pos-1] = digits[pos-1] - 1
      digits[pos] = 9
      pos = pos - 1
  while digits[0] == 0:
    digits.pop(0)
  result = ''.join([str(x) for x in digits])
  print("Case #{}: {}".format(i, result))