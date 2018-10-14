#!/usr/bin/env python3

from sys import stdin

def solve(ifs):
  N = int(ifs.readline())
  rdigits = []
  while N > 0:
    rdigits.append(N % 10)
    N = N // 10

  digits = [rdigits[-i] for i in range(1, len(rdigits) + 1)]

  i = 0
  while i + 1 < len(digits):
    if digits[i] > digits[i+1]:
      digits[i] = digits[i] - 1
      for j in range(i + 1, len(digits)):
        digits[j] = 9
      if i > 0:
        i -= 1
    else:
      i += 1

  while len(digits) > 1 and digits[0] == 0:
    digits.pop(0)

  return ''.join(str(d) for d in digits)

if __name__ == '__main__':
	T = int(stdin.readline())
	#print(T, 'cases to evaluate')
	for i in range(T):
		result = solve(stdin)
		print('Case #' + str(i + 1) + ': ' + result)
