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
start = {
    1:0,
    2:1,
    3:2,
    4:3,
    5:4,
    6:5,
    7:6,
    8:7,
    9:8,
    10:9,
    100: 28,
    1000: 137,
    10000: 336,
    100000: 1435,
    1000000: 3434,
    10000000: 14433,
    100000000: 34432,
    1000000000: 144431,
    10000000000: 344430,
    100000000000: 1444429,
    1000000000000: 3444428,
    10000000000000: 14444427,
    100000000000000: 34444426,
}

def findz(n):
    if(n in start):
        return start[n]
    if(n%10 == 0):
        return findz(n-1)+1
    l = len(str(n))
    m = l//2
    left = int(str(n)[:m][::-1])-1
    right = int(str(n)[m:])
    base = 10**(l-1)
    calc = findz(base)+right+left+(1 if left!=0 else 0)
    return calc

for t in range(scan()):
    print('Case #%d: %d'%(t+1,findz(scan())+1))


if ofg:
 sys.stdout.flush()
 sys.stdout.close()
 sys.stderr.write("OK\n")