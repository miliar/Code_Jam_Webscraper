# link: https://code.google.com/codejam/contest/5314486/dashboard#s=0
import string
import time

testIndex=1

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/round2"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(int,line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
for case in xrange(inputData[0][0]):
  n,p=inputData[case*2+1]
  arr=[0]*p
  for a in inputData[case*2+2]:
    arr[a%p]+=1
  if p==2:
    fileToWrite.write("Case #"+str(case+1)+": "+str((arr[1]-1)/2+1+arr[0])+"\n")
  elif p==3:
    pairs=min(arr[1],arr[2])
    left=arr[1]+arr[2]-2*pairs
    fileToWrite.write("Case #"+str(case+1)+": "+str((left-1)/3+1+pairs+arr[0])+"\n")
  else:
    pairs=min(arr[1],arr[3])
    left=arr[1]+arr[3]-2*pairs
    pairs+=arr[2]/2
    if arr[2]%2==1 and left>=2:
      pairs+=1
      left-=2
    fileToWrite.write("Case #"+str(case+1)+": "+str((left-1)/4+1+pairs+arr[0])+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
