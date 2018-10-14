from math import pi #面積計算

T=int(input())
for roop in range(T):
	temp=input().split()
	N=int(temp[0])
	K=int(temp[1])
	RH=[[int(j) for j in input().split()] for i in range(N)]
	ans=0
	
	#側面積計算
	sideSquare=[[2*pi*RH[i][0]*RH[i][1],RH[i][0],i] for i in range(N)]
	sideSquare.sort()
	sideSquare.reverse()
	
	
	#全ての種類をとりあえず一番下にして考える
	for i in range(N):
		bottom=RH[i][0]
		tempAns=2*pi*bottom*RH[i][1] + pi*bottom*bottom
		#使用個数
		use=1
		index=0
		while index<N and use<K:
			#一番下じゃない　and 一番下に変わらない
			if sideSquare[index][2]!=i and sideSquare[index][1]<=bottom:
				tempAns+=sideSquare[index][0]
				use+=1
			index+=1
		ans=max(ans,tempAns)
	
	print("Case #"+str(roop+1)+": "+str(ans))