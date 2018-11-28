n = int(input())
for i in range (1, n+1):
	num = int(input())
	for j in range (num, 0, -1):
		list = [int(i) for i in str(j)]
		if sorted(list)==list:
			print("Case #",i,": ",j, sep='')
			flag=1
			break

