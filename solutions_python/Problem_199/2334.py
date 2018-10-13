def is_happy(s):
  for i in s:
    if i == '-':
      return False
  return True


def flip(s, start, length):
  for i in xrange(start, start + length):
    s[i] = '-' if s[i] == '+' else '+'
  return s


def getMinFlips(s, k):
   number_of_flips = 0
   list_s = list(s)
   for i in xrange(0, len(s) - k + 1, 1):
     if list_s[i] == '-':
       list_s = flip(list_s, i, k);
       number_of_flips+=1;
   if is_happy(list_s):
     return number_of_flips
   return "IMPOSSIBLE"

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s, k = [s for s in raw_input().split(" ")]
  k = int(k)
  result = getMinFlips(s, k)
  print "Case #{}: {}".format(i, result)

