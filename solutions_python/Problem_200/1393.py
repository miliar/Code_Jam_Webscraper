#!/usr/bin/python3
num_cases = int(input())
for i in range(0,num_cases):
  str_N = input()
  N = int(str_N)
  digits = list(str_N)
  j = 0
  while j < len(digits) - 1:
    if int(digits[j]) > int(digits[j + 1]):
      beginning = j
      k = j
      while k > 0:
        if int(digits[k]) == int(digits[k - 1]):
          beginning = k - 1
          k -= 1
        else:
          break
      N -= int("".join(digits[beginning + 1:])) + 1
      break
    else:
      j += 1
  print("Case #{}: {}".format(i + 1, N))
