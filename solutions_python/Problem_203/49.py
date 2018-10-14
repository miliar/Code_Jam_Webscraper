# link: https://code.google.com/codejam/contest/5304486/dashboard#s=p0
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2017/round1A"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[line.split() for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
lineidx=1
for case in xrange(int(inputData[0][0])):
  R,C=map(int,inputData[lineidx])
  res=[]
  fst=0
  for i in xrange(R):
    tmp=list(inputData[lineidx+1+i][0])
    if tmp==['?']*C:
      if res:
        res.append(res[-1])
      else:
        fst+=1
    else:
      i=0
      while tmp[i]=='?':
        i+=1
      ch=tmp[i]
      for i in xrange(C):
        if tmp[i]=='?':
          tmp[i]=ch
        else:
          ch=tmp[i]
      line="".join(tmp)
      while fst>0:
        res.append(line)
        fst-=1
      res.append(line)
  fileToWrite.write("Case #"+str(case+1)+": \n")
  for i in xrange(R):
    fileToWrite.write(res[i]+"\n")
  lineidx+=1+R
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
