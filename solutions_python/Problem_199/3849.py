def flip(s,x):
  chars=list(s)
  j=1
  i_prev=0
  count=0
  x2=x-1
  i=0
  try:
    while i<=(len(chars)-x2):
      if check(chars)==True:
        return count
      i_prev = i
      if chars[i] is '-':
        chars[i]='+'
        while j <= (x-1):
          i+=1
          if chars[i] is '-':
            chars[i]='+'
          else:
            chars[i]='-'
          j+=1
        j=1
        count+=1
      i=i_prev
      i+=1
  except:
    return -1
  return -1

def check(charac):
  if '-' in charac:
    return False
  else:
    return True


def printl():
  t =int(raw_input())
  for i in range(1,t+1):
    cad, part = [str(s)for s in raw_input().split(" ")]
    if flip(cad,int(part)) == -1:
      print "Case #{}: {}".format(i, 'IMPOSSIBLE')
    else:
      print "Case #{}: {}".format(i, flip(cad,int(part)))

 # # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
 # # This is all you need for most Google Code Jam problems.
 # t = int(raw_input())  # read a line with a single integer
 # for i in xrange(1, t + 1):
 #     # read a list of integers, 2 in this case
 #
 #   # check out .format's specification for more formatting options

printl()
