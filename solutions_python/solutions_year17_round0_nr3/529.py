# link: https://code.google.com/codejam/contest/3264486/dashboard#s=p2
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/quali"
problemName="C"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(int,line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
for case in xrange(inputData[0][0]):
  N,K=inputData[case+1]
  nums={N:1}
  nxt=N
  while K>nums[nxt]:
    num=nums.pop(nxt)
    K-=num
    if nxt%2==1:
      if nxt/2 in nums:
        nums[nxt/2]+=num*2
      else:
        nums[nxt/2]=num*2
    else:
      if nxt/2 in nums:
        nums[nxt/2]+=num
      else:
        nums[nxt/2]=num
      if nxt/2-1 in nums:
        nums[nxt/2-1]+=num
      else:
        nums[nxt/2-1]=num
    nxt=max(nums.keys())
  # last will arrive when the largest is nxt
  solution=str(nxt/2)+" "
  if nxt%2==1:
    solution+=str(nxt/2)
  else:
    solution+=str(nxt/2-1)
  fileToWrite.write("Case #"+str(case+1)+": "+solution+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
