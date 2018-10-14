#!/usr/bin/python

def simplify(s):
  if (len(s) <= 1):
    return s

  #print "DEBUG: Invoked simplify({})".format(s)
  left = s[:-1]
  leftA = left
  if (len(left) > 1):
    left = simplify(left)
    if (int(left) < int(leftA)):
      return left + '9'
    #print "DEBUG: [{}] Changed left={} to left={}".format(s, leftA, left)

  right = s[-1]
  left_last = left[-1]

  #print "DEBUG: ({}) left:{}, right:{}".format(s, left, right)

  if (int(left_last) > int(right)):
    # must set right to 9 and reduce left_last by one 
    # and then simplify
    right = '9'
    left = str(int(left) - 1)
    left = simplify(left)
    return left + right
  elif (int(left_last) < int(right)):
    #left = simplify(left)
    return left + right
  else:
    # equals case
    # first simplify left
    # then return simplify(left+right)?
    left1 = left
    #print "DEBUG: recursively calling simplify({})".format(left1)
    #left = simplify(left)
    #print "DEBUG: recursively calling simplify({}) returned {}".format(left1, left)
    left_last = left[-1]
    if (int(left_last) <= int(right)):
      return left + right
    else:
      #print "DEBUG: Again recursively calling simplify({})".format(left + right)
      s2 = left + '9'
      #print "DEBUG: Again recursively calling simplify({}) returned {}".format(left + right, s2)
      return s2

def main():
  # read a line with a single integer
  t = int(raw_input())
  for i in xrange(1, t + 1):
    # read a list of integers, 1 in this case
    nlist = [int(s) for s in raw_input().split(" ")]
    n = nlist[0]
    s = str(n)
    ss = simplify(s)
    sss = int(ss)
    #print "DEBUG: s=[{}], ss=[{}]".format(s, sss)
    print "Case #{}: {}".format(i, sss)

main()
