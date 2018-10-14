


for _ in range(1,int(input())+1):
	a1,a2 = input().strip().split(' ')
	d,n = [int(a1),int(a2)]
	cnt =0
	for j in range(n):
		#a,a3 = input().strip().split(' ')
	 	k,s = map(int,input().split())
	 	temp = (d-k)/s
	 	if(temp >cnt):
	 		cnt = temp
	print("Case "+ " #"+ str(_) +": ",end = "")
	print("{0:.6f}"  .format(d/cnt))