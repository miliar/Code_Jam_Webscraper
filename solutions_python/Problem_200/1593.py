# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = long(input())  # read a line with a single longeger
for i in range(1, t + 1):
  s = [str(s) for s in raw_input().split(" ")]
  s = list(s[0])
  for j in range(len(s)-1):
     if(int(s[j]) > int(s[j+1])):
         s[j] = str(int(s[j])-1)
         for m in range(len(s)-j-1):
             s[j+m+1] = '9'
         while(int(s[j]) < int(s[j-1]) and j > 0):
             s[j-1] = str(int(s[j-1]) - 1)
             s[j] = '9'
             j = j - 1
         if(s[0] == '0'):
             s = s[1:]
         break
  print("Case #{}: {}".format(i, ''.join(s)))

  # n, m = [long(s) for s in input().split(" ")]  # read a list of longegers, 2 in this case
  #print("Case #{}: {}".format(i, o))
  # check out .format's specification for more formatting options
