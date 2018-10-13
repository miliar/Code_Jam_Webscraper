# link: https://code.google.com/codejam/contest/3264486/dashboard
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/quali"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[line.split() for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
for case in xrange(int(inputData[0][0])):
  st=inputData[case+1][0]
  K=int(inputData[case+1][1])
  arr=[]
  for ch in st:
    arr.append(ch=='+')
  res=0
  for i in xrange(len(st)-K+1):
    if not arr[i]:
      res+=1
      for j in xrange(K):
        arr[i+j]=not arr[i+j]
  if False in arr:
    solution="IMPOSSIBLE"
  else:
    solution=str(res)
  fileToWrite.write("Case #"+str(case+1)+": "+solution+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
