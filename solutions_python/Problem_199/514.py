import sys

def all_happy(s):
  return all(value == "+" for value in s)

def all_sad(s):
  return all(value == "-" for value in s)

def reverse(piece):
  if piece == "+":
    return "-"
  else:
    return "+"

def flip(cake,n,size):
  tmp = cake[:n]
  tmp2 = map(reverse , cake[n:n+size])
  tmp3 = cake[n+size:]
  return tmp + "".join(tmp2) + tmp3

def impossible_pattern(pancake, size):
  if pancake is None:
    return True
  if len(pancake) < size:
    return True
  pattern1 = ""
  pattern2 = ""
  for i in range(0,len(pancake)):
    if i % 2 == 0:
      pattern1 = pattern1 + "-"
      pattern2 = pattern2 + "+"
    else:
      pattern1 = pattern1 + "+"
      pattern2 = pattern2 + "-"
  if pancake == pattern1 or pancake == pattern2:
    return False
  if all_sad(pancake):
    n = divmod(len(pancake), size)
    if n[1] > 0:
      return True
  return False

def pancake_flipper(pancake, size):
  for i in range(0,len(pancake)-size+1):
    if pancake[i] == "-":
      return flip(pancake,i, size)

def process(pancake, size):
  count = 0
  impossible = impossible_pattern(pancake, size)
  while not impossible and not all_happy(pancake):
    pancake = pancake_flipper(pancake, size)
    count += 1
    impossible = impossible_pattern(pancake, size)
  if(impossible):
    return "IMPOSSIBLE"
  else:
    return count

name = "A-large"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

print T
for t in xrange(T):
    line = f.readline().strip().split(' ')
    pancake = str(line[0])
    size = int(line[1])
    res = process(pancake, size)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
