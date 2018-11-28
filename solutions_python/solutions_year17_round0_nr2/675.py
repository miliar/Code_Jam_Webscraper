def is_valid(i):
  s = str(i) if not isinstance(i,str) else i
  # also valid when len(s) == 1
  return all( [ s[k] >= s[k-1] for k in range(1,len(s)) ] )

def naive_solution(i):
  return (i for i in xrange(i, 0, -1) if is_valid(i) ).next()

def more_efficient(s):
  """
  skim through string representation of number from left to right
  whenever a non-tidy pair is found, for instance at positions i and i+1:
    - "reset" all digits starting at i+1 to 9,
    - digit i <- decrement by one if > 0 else (9 and propagate carry)
  """
  def decrease_left(s, pos):
    #print "in decrease_left - %i -- %s" % (pos,s)
    if ( (pos > 0) and (s[pos] != "0") ):
      return s[:pos] + chr( ord(s[pos]) -1 ) + s[pos+1:]
    elif ( (pos == 0) and (s[0] != "1") ):
      return chr( ord(s[pos]) -1 ) + s[1:]
    elif pos == 0:
      # e.g. 1000 -> 999
      return '9' * (len(s) - 1)
    else:
      s = s[:pos] + '9' + s[pos+1:]
      # carry on the decrement
      return decrease_left(s, pos-1)

  def increase_right(s,pos):
    return s[:pos+1] + '9' * (len(s) -pos -1)

  for k in range(1, len(s)):
    if s[k] < s[k-1]:
      s = decrease_left(s,k)
      s = increase_right(s,k)
      # depth is "controlled", called at most one per digit in s
      return more_efficient(s)
  return s

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  m = raw_input()
  print "Case #{}: {} ".format(i, more_efficient(m))

