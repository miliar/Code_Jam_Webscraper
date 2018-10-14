import re

f = open("A-small-attempt3.in","r")
C = int(f.readline())
devices = []

def init(devices,N):
	devices.append([1,"OFF"])
	for i in range(N-1):
		devices.append([0,"OFF"])

def snap(devices,N):
	i = N-1
	while(i>=0):
		if(devices[i][0] == 1):
			if(devices[i][1] == "ON"):
				devices[i][1] = "OFF"
			else:
				devices[i][1] = "ON"
		i = i-1
	for i in range(N):
		if(i!=N-1 and devices[i][0] == 0):
			devices[i+1][0] = 0
		if(i!=N-1 and devices[i][0] == 1 and devices[i][1] == "ON"):
			devices[i+1][0] = 1
		if(i!=N-1 and devices[i][0] == 1 and devices[i][1] == "OFF"):
			devices[i+1][0] = 0

def snaps(devices,K,N):
	for i in range(K):
		snap(devices,N)
		#print(devices)

def light(devices):
	if (devices[len(devices)-1][1] == "ON" and devices[len(devices)-1][0] == 1):
		return "ON"
	return "OFF"

w = open("A-small-attempt3.out","w+")
for i in range(C):
	devices = []
	N, K = map(int,f.readline().split())
	init(devices,N)
	#print(devices)
	snaps(devices,K,N)
	if (i==C-1):
		w.write('Case #%d: %s' % ((i+1),light(devices)))
	else:
		w.write('Case #%d: %s\n' % ((i+1),light(devices)))

f.close()
w.close()