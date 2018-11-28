from math import sqrt

strin = open("in.txt","r").read().split('\n')
strin = filter(None, strin)

palindromes = []
fairsquares = []
total = int(strin[0])

def is_palindrome(n):
  if n in palindromes:
    return True
  else:
    s = str(n)
    if s == s[::-1]:
      palindromes.append(n)
      return True
    else:
      return False

def is_sqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def run_fairsquare(n):
  if is_palindrome(n):
    sq = is_sqrt(n)
    if sq*sq == n and is_palindrome(sq):
      fairsquares.append(sq)

def parse_range(r):
  del fairsquares[:]
  s = strin[r+1]
  lh = s.split(' ')
  out = "Case #" + str(r+1) + ": "
  for i in range(int(lh[0]),int(lh[1])+1):
    run_fairsquare(i)
  out += str(len(fairsquares))
  return out

final = ""
for i in range(total):
  final += parse_range(i) + "\n"

with open("out.txt","w") as txt_file:
  txt_file.write(final)
