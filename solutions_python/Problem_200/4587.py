def solve(n):
  l= len(n)
  if(l==1): return n
  original=int(n)
  last=9
  rev=n[::-1]
  num=int(n)
  for i in range(l):
    prev=int(str(num)[l-1-i])
    if prev==0:
      num-=10**i
  other=str(num)
  l=len(n)
  rem=l
  for i in range(l-1):
    if n[i+1]<n[i]:
      n=n[:i]+str(int(n[i])-1)
      j=i
      while j<0: 
        while n[j]>n[j-1]:
          n=n[:j]+str(int(n[j])-1)+n[j+1:]
        j-=1
      rem=i+1
      break
  while rem<l:
    n+='9'
    rem+=1

  



  while n[1]<n[0]:
    n=str(int(n[0])-1)+n[1:]

  for i in range(l-1):
    i=l-i-1
    for j in range(9):
      #print i,j,n,int(n[:i]+str(9-j)+n[i+1:]),i>0 and 9-j>=int(n[i-1]) and int(n[:i]+str(9-j)+n[i+1:]) <= original
      if i+1<l and 9-j<=int(n[i+1]) and int(n[:i]+str(9-j)+n[i+1:]) <= original:
          n=n[:i]+str(int(9-j))+n[i+1:]
          break

  #n=str(int(n))
  #if len(str(int(n)))+1<l: n='9'+n
  
  """if any(n[i+1]<n[i] for i in range(l-1)) or int(n)>original:
    print 'Error: {} --> {}'.format(original,n)
  alt=str(int(n)+1)
  if (all(int(alt[i+1])>=int(alt[i]) for i in range(len(alt)-1)) and int(alt)<=original):
      #print([(alt[i+1],alt[i]) for i in range(l-1)])
      print 'Error: {} --> {} but {}'.format(original,n,alt)
      #n=alt"""
  return n

t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
  n = raw_input()
  print "Case #{}: {}".format(tt, int(solve(n)))#,'from '+n
#for n in range(1000):
  #print "Case #{}: {}".format(n+1, solve(str(n+1)))