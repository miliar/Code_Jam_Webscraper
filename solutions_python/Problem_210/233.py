import sys
T=int(input())
for roop in range(T):
	temp=input().split()
	AC=int(temp[0])
	AJ=int(temp[1])
	C=[[int(j) for j in input().split()] for i in range(AC)]
	J=[[int(j) for j in input().split()] for i in range(AJ)]
	C.sort()
	J.sort()
	startC=[C[i][0] for i in range(AC)]
	startJ=[J[i][0] for i in range(AJ)]
	#合計育児時間
	timeC=0
	timeJ=0
	#一個前の自分の開始時間
	beforeC=0
	beforeJ=0
	
	#0=空白　1,Cの後　2,Jの後
	flag=0
	ans=0
	margine=0
	#print(C)
	if AC+AJ==1:
		ans=2
	else:
		if AC==2:
			if C[1][1]-C[0][0]>60*12 and C[0][1]+(60*24 - C[1][0])>60*12:
				ans=4
			else:
				ans=2
		elif AJ==2:
			if J[1][1]-J[0][0]>60*12 and J[0][1]+(60*24 - J[1][0])>60*12:
				ans=4
			else:
				ans=2
		else:
			ans=2
	
	print("Case #"+str(roop+1)+": "+str(ans))