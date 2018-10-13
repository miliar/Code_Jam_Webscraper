import re
import sys
buf=[]
def scans():
 global buf
 while 1:
  while len(buf) <= 0: buf=input().replace('\n',' ').split(' ')
  o=buf.pop(0)
  if o!='': break
 return o
def scan(): return int(scans())

sys.stdin = open('input.txt')
ofg=1
if ofg:
 sys.stdout = open('output.txt','w')


#Code Here
def calc(hikers):
    if(len(hikers)<2):
        return 0
    if(len(hikers)>2):
        sys.stderr.write("HIKER OVERLOAD!\n")
        return 0
    end1 = hikers[0][2]*(1-hikers[0][0]/360)
    end2 = hikers[1][2]*(1-hikers[1][0]/360)
    end3 = hikers[0][2]*(1-hikers[0][0]/360+1)
    end4 = hikers[1][2]*(1-hikers[1][0]/360+1)
    # print(end1,end2,end3,end4)
    if(end3-end2<0.00001):
        return 1
    if(end4-end1<0.00001):
        return 1
    return 0

for t in range(scan()):
    hikers = [(scan(),scan(),scan()) for i in range(scan())]
    print('Case #%d: %d'%(t+1,calc(hikers)))


if ofg:
 sys.stdout.flush()
 sys.stdout.close()
 sys.stderr.write("OK\n")