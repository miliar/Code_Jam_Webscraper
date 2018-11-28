#! /usr/bin/env python3

import math

def generatePalindromes(cur, length, multiplier):
  #print("cur: {0}, length: {1}, multiplier: {2}".format(cur, length, multiplier))
  if length == 0:
    yield cur
  elif length == 1:
    for digit in range(1, 3):
      yield digit
  elif length == 2:
    for digit in range(1, 3):
      for palindrome in generatePalindromes((cur + digit * multiplier) * 10 + digit, length - 2, multiplier * 100):
        yield palindrome
  elif length % 2 == 1:
    for digit in range(0, 3):
      for palindrome in generatePalindromes(digit, length - 1, multiplier * 10):
        yield palindrome
  else:
    for digit in range(0, 3):
      for palindrome in generatePalindromes((cur + digit * multiplier) * 10 + digit, length - 2, multiplier * 100):
        yield palindrome

def generatePalindromeRange(lowerLength, upperLength):
  for length in range(lowerLength, upperLength + 1):
    #print("length: {0}".format(length))
    for palindrome in generatePalindromes(0, length, 1):
      yield palindrome

def convertToNumber(digits):
  result = 0;
  for digit in digits:
    result *= 10
    result += digit
  return result

def convertToDigitList(number):
  result = []
  while number > 0:
    result.append(number % 10)
    number //= 10
  return result

def isPalindrome(digits):
  for i in range(0, len(digits) // 2):
    if digits[i] != digits[len(digits) - 1 - i]:
      return False
  return True

def isPalindromeNumber(number):
  power = math.floor(math.log10(number))
  exp = 10 ** power
  while number > 0:
    first = number // exp
    last = number % 10
    if first != last:
      return False
    number %= exp
    number /= 10
  return True

def countFairSquares(A, B):
  count = 0
  lower = math.floor(math.sqrt(A))
  upper = math.ceil(math.sqrt(B))
  lowerLength = max(math.floor(math.log10(math.sqrt(A))), 1)
  upperLength = max(math.ceil(math.log10(math.sqrt(B))), 1)
  for palindrome in generatePalindromeRange(lowerLength, upperLength):
    #print("trying {0}".format(palindrome))
    if palindrome < lower or palindrome > upper:
      continue
    square = palindrome ** 2
    if square < A or square > B:
      continue
    digits = convertToDigitList(square)
    if isPalindrome(digits):
      #print(str(palindrome) + " ^ 2 = " + str(square))
      count += 1
  if A <= 9 <= B:
    count += 1 
  return count      

def processCase(i):
  line = input()
  limits = line.split()
  A = int(limits[0])
  B = int(limits[1])
  print("Case #" + str(i) + ": " + str(countFairSquares(A, B)))

def main():
  line = input()
  if line:
    number = int(line)
    for i in range(number):
      processCase(i + 1)

main()
