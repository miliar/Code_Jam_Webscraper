# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer


for i in range(1, t + 1):
  n = str(input().strip())
  a = list(int(x) for x in n )
  for k in range(len(a)-1):
    if a[k] > a[k+1]:
      if k!=0 and a[k] == a[k-1]:
        a[0]=a[k]-1
        for j in range(1,len(a)):
          a[j] = 9
        break
      else:
        a[k]-=1
        if a[k] == 0:
          for l in range(len(a)):
            a[l] = 9
          del a[-1]
          break
        for j in range(k+1, len(a)):
          a[j] = 9
    
      
  ans = int(''.join(map(str,a)))
  print('Case #{}: {}'.format(i, ans))
 
