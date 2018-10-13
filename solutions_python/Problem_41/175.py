
def isNextNum(numStr,nums,x):
  string = str(x)
  d = dict()
  for l in string:
    if l == '0':
      continue
    if l in d:
      d[l] = d[l]+1
    else:
      d[l] = 1
  #print d
  if d == nums:
    return 1
  else:
    return 0

def getNextInt(numStr, nums, num):
  target = num +1
  while isNextNum(numStr,nums,target)== 0:
    target +=1
    #print target
  return target
  

inputFile = open('small-B.in','r')
outputFile = open('small-B.out','w')
numTc = int(inputFile.readline())
for i in range(0,numTc):
  numStr = inputFile.readline().strip()
  #print numStr
  nums = dict()
  for l in numStr:
    if l == '0':
      continue
    if l in nums:
      nums[l] = nums[l]+1
    else:
      nums[l] = 1
  print i
  num = int(numStr)
  #print "Case #%s: " % str(i+1),
  #print "%s" % getNextInt(numStr,nums,num)
  line = "Case #%s: %s" %(str(i+1),getNextInt(numStr,nums,num))
  outputFile.write(line +"\n")
outputFile.close()
inputFile.close()
  
