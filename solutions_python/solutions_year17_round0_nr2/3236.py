def getArrayWithDigits(input):
    digits = []
    for digit in input:
        digits.append(int(digit))
    return digits[::-1]

def removeLeadingZeros(digits):
    result = []
    i = 0
    while digits[i] == 0:
        i += 1
    for j in range(i, len(digits)):
        result.append(digits[j])
    return result

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  digits = getArrayWithDigits(input())
  isChanging = True
  while isChanging:
      isChanging = False
      for j in range(0, len(digits) - 1):
          if digits[j] - digits[j+1] < 0:
              digits[j] = 9
              digits[j+1] -= 1
              for k in range(0, j):
                  digits[k] = 9
              isChanging = True
  result = removeLeadingZeros(digits[::-1])
  print("Case #{}: {}".format(i, ''.join(map(str, result))))
