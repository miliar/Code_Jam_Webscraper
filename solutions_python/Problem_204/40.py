# link: https://code.google.com/codejam/contest/5304486/dashboard#s=p1
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/round1A"
problemName="B"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(int,line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
lineidx=1
for case in xrange(inputData[0][0]):
  N,P=inputData[lineidx]
  need=inputData[lineidx+1]
  arr=[]
  for i in xrange(N):
    inputData[lineidx+2+i].sort(reverse=True)
    arr.append(inputData[lineidx+2+i])
  lineidx+=2+N
  done=False
  res=0
  por=0
  while not done:
    for i in xrange(N):
      por=max(por,int(arr[i][-1]/(need[i]*1.1)))
    OK=True
    for i in xrange(N):
      while not done and arr[i] and arr[i][-1]<por*need[i]*0.9:
        arr[i].pop()
      if not arr[i]:
        done=True
      if done or not need[i]*por*0.9<=arr[i][-1]<=need[i]*por*1.1:
        OK=False
    if OK:
      res+=1
      for i in xrange(N):
        arr[i].pop()
        if not arr[i]:
          done=True
    else:
      por+=1
  fileToWrite.write("Case #"+str(case+1)+": "+str(res)+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
