import numpy as np
import time
start_time = time.time()

f = open('A-large.in','r')
output = open('output.txt','w')
N=int(f.readline())
ones=np.ones(shape=(4,1))
for i in range(N):
	index=0
	a=np.zeros(16)
	b=np.zeros(16)
	dataline = f.readline().rstrip()
	output.write('Case #'+str(i+1)+': ')

	while dataline!="":
		for c in list(dataline):
			if c == "T":
				a[index]=-1
				b[index]=+1
			elif c == "X":
				a[index]=-1
				b[index]=-1
			elif c == "O":
				a[index]=1
				b[index]=1
			elif c == ".":
				a[index]=0
				b[index]=0
			index+=1
		dataline = f.readline().rstrip()
	a.resize((4,4))
	b.resize((4,4))
	at=a.transpose()
	bt=b.transpose()
	aones=a.dot(ones)
	bones=b.dot(ones)
	atones=at.dot(ones)
	btones=bt.dot(ones)
	if (np.max(np.maximum(aones*aones,atones*atones)) == 16) | (np.max(np.maximum(bones*bones,btones*btones)) == 16):
		if (np.max(np.maximum(aones,atones)) == 4) | (np.max(np.maximum(bones,btones)) == 4):
			output.write('O won\n')
		else :
			output.write('X won\n')
	elif (np.asscalar(a.diagonal().dot(ones)) == 4) | (np.asscalar(a[::-1].diagonal().dot(ones)) == 4) | (np.asscalar(b.diagonal().dot(ones)) == 4) | (np.asscalar(b[::-1].diagonal().dot(ones)) == 4):
		output.write('O won\n')
	elif (np.asscalar(a.diagonal().dot(ones)) == -4) | (np.asscalar(a[::-1].diagonal().dot(ones)) == -4) | (np.asscalar(b.diagonal().dot(ones)) == -4) | (np.asscalar(b[::-1].diagonal().dot(ones)) == -4):
		output.write('X won\n')
	elif a.prod()==0:
		output.write('Game has not completed\n')
	else :
		output.write('Draw\n')
	print "progress : "+str(i)+" / "+str(N)+"\n"
elapsed_time = time.time() - start_time
print "Elapsed Time: "+str(elapsed_time)+"\nAverage Elapsed Time per case: "+str(elapsed_time/N)+"\n"
	






