import re
import sys
import random
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())

sys.stdin = open('input.txt')
ofg=1
if ofg:
	sys.stdout = open('output.txt','w')
for t in range(scan()):
	mint = 99999
	arr = [scan() for i in range(scan())]
	if all(i<=0 for i in arr):
		print('Case #%d: %d'%(t+1,0))
	for target in range(1,max(arr)+1):
		spm = 0
		for i in arr:
			spm+=(i-1)//target
		#print('@Tar=%d V=%d'%(target,target+spm))
		mint = min(mint,spm+target)
	print('Case #%d: %d'%(t+1,mint))
	sys.stderr.write('@%d '%(t+1))
if ofg:
	sys.stdout.flush()
	sys.stdout.close()