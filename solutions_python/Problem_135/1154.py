import sys

one = two = []
common = []

def solve(one, two):
  global common
  common = []
  for i in xrange(4):
    if one[i] in two:
      common += [one[i]]

def main():
  T = int(sys.stdin.readline())
  for i in xrange(T):
    global one, two
    row = int(sys.stdin.readline())
    for j in xrange(1,5):
      if row == j:
        one = [int(x) for x in sys.stdin.readline().split()]
      else:
        sys.stdin.readline()
    
    row = int(sys.stdin.readline())
    for j in xrange(1,5):
      if row == j:
        two = [int(x) for x in sys.stdin.readline().split()]
      else:
        sys.stdin.readline()
    
    solve(one, two)

    if len(common) == 1:
      answer = common[0]
    elif len(common) == 0:
      answer = "Volunteer cheated!"
    else:
      answer = "Bad magician!"

    print "Case #%d: %s" % (i+1, answer)

main()