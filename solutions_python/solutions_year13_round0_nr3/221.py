from sys import stdin
import bisect

def is_palindrome(palindrome):
  for i in range(len(palindrome) / 2):
    if palindrome[i] != palindrome[-i-1]:
      return False
  return True

def generate(length, init_len, pre, ones, middle=''):
  global palindromes
  if length > 1:
    start = 1 if length == init_len else 0
    end = 3 if length == init_len else (2 if ones < 4 else 1)
    for i in range(start, end):
      if not generate(length - 2, init_len, pre + str(i), ones + (1 if i == 1 else 0)):
        return False
  elif length > 0:
    for i in range(4):
      if not generate(0, init_len, pre, ones, middle=str(i)):
        return False
  else:
    n = int(pre + middle + pre[::-1]) ** 2
    if (n > 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
      return False
    if is_palindrome(str(n)):
      palindromes.append(n)
  return True

palindromes = []

for i in range (1, 60):
  if not generate(i, i, '', 0):
    break

n = int(stdin.readline())
for i in range(n):
  line = stdin.readline().split()
  A = int(line[0])
  B = int(line[1])
  count = 0
  for p in range(bisect.bisect_left(palindromes, A), bisect.bisect_right(palindromes, B)):
    if A <= palindromes[p] <= B:
      count += 1
  print 'Case #' + str(i + 1) + ':', count

