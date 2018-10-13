
T = int(raw_input())
for t in range(T):
	dados=raw_input().split()
	d=[]
	for i in dados:
		d.append(int(i))
	gah=False
	if d[0]==1:
		gah=True
	elif d[0]==4:
		gah=d[1]*d[2]>11
	else: 
		gah=(d[1]*d[2])%d[0]==0
		if d[0]==3 and (max(d[1],d[2])<3 or min(d[1],d[2])<2):
			gah=False
	if gah:
		ganhador="GABRIEL"
	else:
		ganhador="RICHARD"
	
	print("Case #" + str(t+1) + ": " + ganhador)
