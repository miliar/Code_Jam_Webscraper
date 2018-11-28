# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = long(input())  # read a line with a single longeger
for i in range(1, t + 1):
  s, k = [str(s) for s in raw_input().split(" ")]
  s = list(s)
  k = int(k)
  cnt = 0
  for j in range(len(s) - k + 1):
     if(s[j] == '-'):
         cnt = cnt + 1
         for m in range(k):
             if(s[j+m] == '-'):
                 s[j+m] = '+'
             else:
                 s[j+m] = '-'
  if('-' in s[-k+1:]):
      print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
  else:
      print("Case #{}: {}".format(i, cnt))

  # n, m = [long(s) for s in input().split(" ")]  # read a list of longegers, 2 in this case
  #print("Case #{}: {}".format(i, o))
  # check out .format's specification for more formatting options
