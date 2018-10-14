# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
  #n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  n = int(input())
  m = list(str(n))
  for i in range(len(m)-1,0,-1):
        if int(m[i]) < int(m[i-1]):
              for j in range(i,len(m),1):
                    m[j]='9'
              m[i-1]=str(int(m[i-1])-1)
  print('Case #'+str(k)+': '+str(int(''.join(m))))
