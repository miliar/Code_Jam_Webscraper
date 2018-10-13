import numpy as np
import time
start_time = time.time()

f = open('B-large.in','r')
input_data=f.readlines()[::-1]
f.close()
output = open('B-output.txt','w')

T=int(input_data.pop().rstrip())

for case in range(T):
	print("Progress : " +str(case+1)+" / "+str(T)+"\033[F")

	output.write('Case #'+str(case+1)+': ')
	lawn=""
	lawn_size = np.array(map(int, input_data.pop().rstrip().split()))
	
	for lines in range(lawn_size[0]):
		lawn+=input_data.pop().rstrip()+" "
	lawn=np.array(map(int, lawn.split()))
	lawn.resize(lawn_size)

	simul=np.ones(lawn_size)*lawn.max()
	for height in range(1,lawn.max())[::-1]:
		simul[np.where((lawn<=height).dot(np.ones(lawn_size[1]))==lawn_size[1]),:]=height
		simul[:,np.where((lawn<=height).T.dot(np.ones(lawn_size[0]))==lawn_size[0])]=height
	if (simul==lawn).all():
		output.write("YES\n")
	else:
		output.write("NO\n")

elapsed_time = time.time() - start_time
print "\nElapsed Time: "+str(elapsed_time)+"\nAverage Elapsed Time per case: "+str(elapsed_time/T)+"\n"