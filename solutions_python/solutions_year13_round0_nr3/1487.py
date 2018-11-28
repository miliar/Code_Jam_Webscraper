# Google Code Jam 2013
# Problem C. Fair and Square

fair = []
#Power = 24
Power = 10

def generate2():
  fair.append(1)
  fair.append(4)
  fair.append(9)
  p = 1
  base = 1
  odd = False
  while p <= Power:

    x = base
    this_base = base * 2

    while x < this_base:
      s = get_palindrome2(x, odd)
      q = s*s
      if is_palindrome(q):
        fair.append(q)
      x += 1

    if not odd:
      s = '2'
      for i in range(p-1):
        s += '0'
      q = int(s + s[-1::-1])

      q = q*q

      if is_palindrome(q):
        fair.append(q)
      base *= 2
      p += 1

    odd = not odd


def get_palindrome2(x, odd):
  s = bin(x)[2:]

  r = s

  if odd:
    r += s[-1:0:-1]
  else:
    r += s[-1::-1]

  return int(r)

def is_palindrome(x):
  s = str(x)
  m = len(s) - 1
  i = 0

  while i <= m:
    if s[i] != s[m]:
      return False
    i += 1
    m -= 1

  return True

def generate():
  p = 1
  base = 1
  odd = True
  while p <= Power:

    x = base
    this_base = base * 10

    while x < this_base:
      s = get_palindrome(x, odd)
      q = s*s
      if is_palindrome(q):
        fair.append(q)
      x += 1

    if not odd:
      base *= 10
      p += 1

    odd = not odd

def binary_search(x, a, b):
  if a >= b:
    return b

  c = (a+b)/2

  if x == fair[c]:
    return c
  if x < fair[c]:
    return binary_search(x, a, c)
  return binary_search(x, c+1, b)




cases = int(raw_input())

generate2()

#for i in fair:
#  print i

length = len(fair)

#print len(str(fair[-1]))

for cases_r in range(cases):
  (a, b) = raw_input().split()
  a = int(a)
  b = int(b) + 1

  # print binary_search(a,0,length), binary_search(b,0,length)

  print "Case #%d: %d" %(cases_r + 1, binary_search(b,0,length) - binary_search(a,0,length))


#123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789.
#40000000000800000000004
#400000000000080000000000004
#4000000000000008000000000000004
#40000000000000000000000000000800000000000000000000000000004
#4000000000000000000000000000000000000008000000000000000000000000000000000000004
