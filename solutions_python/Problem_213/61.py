# link: https://code.google.com/codejam/contest/5314486/dashboard#s=1
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/round2"
problemName="B"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(int,line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
lineIdx=1
for case in xrange(inputData[0][0]):
  n,c,m=inputData[lineIdx]
  tick=[0]*n
  cost=[0]*c
  lineIdx+=1
  for i in xrange(m):
    tick[inputData[lineIdx+i][0]-1]+=1
    cost[inputData[lineIdx+i][1]-1]+=1
  lineIdx+=m
  rides=max(cost) # the most ticket at one user
  fstk=0
  for i in xrange(n):
    fstk+=tick[i]
    rides=max(rides,(fstk-1)/(i+1)+1)
  pro=0
  for i in xrange(n):
    if tick[i]>rides:
      pro+=tick[i]-rides
  fileToWrite.write("Case #"+str(case+1)+": "+str(rides)+" "+str(pro)+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
