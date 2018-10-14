import sys
import math

def IN():
  return sys.stdin.readline()

def OUT(txt):
  ERR("[OUT] " + txt)
  sys.stdout.write(txt)
  sys.stdout.flush()

def ERR(txt):
  print >> sys.stderr, txt

ERR("start")

def check_palindrome(num):
  i = 0
  j = len(num) - 1
  while i < j:
    if num[i] != num[j]:
      return False
    i += 1
    j -= 1
  return True

def do_case(num):
  OUT("Case #" + str(num + 1) + ": ")
  lower, upper = tuple(int(x) for x in IN().split())
  good = 0
  for cur in range(lower, upper + 1):
    ERR(cur)
    if not check_palindrome(str(cur)):
      continue
    root = int(math.sqrt(cur))
    if root * root != cur:
      continue
    if not check_palindrome(str(root)):
      continue
    good += 1
  OUT(str(good) + "\n")

for case in range(int(IN())):
  do_case(case)

sys.stdout.flush()
