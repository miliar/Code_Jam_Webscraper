from fractions import gcd

s = open('B-small-attempt2.in','r').read()
out = open('B-small.out','w')

new = s.split('\n')
#print new

n = 0
i = 0

def gcd2(nums):
  d = nums[0]
  for n in nums:
    d = gcd(n,d)
  return d    
  
def lcm(nums):
  if len(nums) == 0:
    return 0
  m = nums[0]
  for n in nums:
    if n == 0:
      continue
    if m % n > 0:
      d = gcd(m,n)
      print 'd',n/d
      print m,n,d
      m *= n/d
      print m
  return m
  
def diff(nums):
  diffs = []
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      if abs(nums[i]-nums[j]) not in diffs:
        diffs.append(abs(nums[i]-nums[j]))
  return diffs    
        
for s in new:
  if n == 0:
    n = int(s)
    continue
  
  s = s.split(' ')
  if len(s) < 2 :
    break
  
  i += 1
  
  C = []
  for k in s:
    C.append(int(k))
  
  del C[0]
  nums = diff(C)
  d = gcd2(nums)
  out1 = 0
  R = []
  for v in C:
    if v%d > 0:
      R.append(d-v%d)
  out1 = lcm(R)
#  print out1  
  out.write("Case #" +str(i)+": "+str(out1)+"\n")
  
  n = n-1
#  print n
  if n == 0:
    break

