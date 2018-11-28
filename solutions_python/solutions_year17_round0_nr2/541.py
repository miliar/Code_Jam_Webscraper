# link: https://code.google.com/codejam/contest/3264486/dashboard#s=p1
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/quali"
problemName="B"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[int(line) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
for case in xrange(inputData[0]):
  N=inputData[case+1]
  nst=str(N)
  lst=len(nst)
  solution=""
  for i in xrange(1,lst):
    if nst[lst-i]<nst[lst-(i+1)]:
      solution="9"*i
      nst=str((N/(10**i))*(10**i)-1)
    else:
      solution=nst[lst-i]+solution
  if len(nst)==lst: # needed because of the eliminated first digit
    solution=nst[0]+solution
  fileToWrite.write("Case #"+str(case+1)+": "+solution+"\n")
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
