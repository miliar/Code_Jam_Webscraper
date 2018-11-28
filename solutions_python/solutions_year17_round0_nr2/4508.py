



def findTidy(List,n):
  if n == 0:
    return List
  elif int(List[n]) < int(List[n-1]):
    List[n-1] = str( int(List[n-1])-1);
    for i in xrange(n,len(List)):
      List[i] = '9';
    return findTidy(List,n-1)
  else:
    return findTidy(List,n-1)



if __name__ == '__main__':
  # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  t = int(raw_input())  # read a line with a single integer
  for i in xrange(1, t + 1):
    # n, m = [int(s) for s in raw_input()]  # read a list of integers, 2 in this case
    x = raw_input()
    n = list(x)
    ans = findTidy(n,len(n)-1)
    ans = ''.join(y for y in ans)
    ans = long(ans)
    print "Case #{}: {}".format(i, ans)
    # check out .format's specification for more formatting options

