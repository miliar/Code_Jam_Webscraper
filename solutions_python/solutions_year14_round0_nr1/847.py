

def entre():
	n=int(raw_input())
	inpute=[[] for i in range(n)]
	outpute=[[] for i in range(n)]
	for i in range(n):
		v=int(raw_input())
		tt=[]
		for x in range(4):
			z=[]
			s=raw_input()
			s=s.split()
			for j in s:
				z.append(int(j))
			tt.append(z)
		vv=int(raw_input())
		ttt=[]
		for x in range(4):
			z=[]
			s=raw_input()
			s=s.split()
			for j in s:
				z.append(int(j))
			ttt.append(z)
		inpute[i]=[[v,tt],[vv,ttt]]
	return inpute,outpute

E,S=entre()

nb=0
for T in E:
	nb+=1
	r=0
	z=0
	ta=T[0][1][T[0][0]-1]
	tb=T[1][1][T[1][0]-1]
	for i in range(4):
		if ta[i] in tb :
			z+=1
			r=ta[i]
	if z==0:
		print("Case #"+str(nb)+": "+"Volunteer cheated!")
	if z>1:
		print("Case #"+str(nb)+": "+"Bad magician!")
	if z==1:
		print("Case #"+str(nb)+": "+str(r))