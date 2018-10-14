import sys
import fractions

i=0
for line in sys.stdin:
  i+=1
  if(i == 1):
    continue

  nums = line.split()[1:];
  gcd = abs(int(nums[0]) - int(nums[1]))
  for j in range(1, len(nums)-1):
    gcd = fractions.gcd(gcd, abs(int(nums[j])-int(nums[j+1])));
  
  min=-1
  for j in range(0, len(nums)):
    if(min==-1 or int(nums[j]) < min): min = int(nums[j])
  min = -min
  while(min<0):
    min += gcd
  print "Case #" + str(i-1) + ": " + str(min)


