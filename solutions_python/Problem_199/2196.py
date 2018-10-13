import sys 
def voltear(entrada,k):
	count=0
	if '-' in entrada:
		for i,x in enumerate(entrada):
			if x == '-':
				if i+k<= len(entrada):
					for j in range (i,i+k):
						if entrada[j] == '-':
							entrada[j] = '+'
						else:
							entrada[j] = '-'
					count+=1
				else:
					if '-' in entrada:
						return -1

	return count

casos=int(sys.stdin.readline().strip())

for x in range(0,casos):
	entrada, k=sys.stdin.readline().strip().split(" ")
	result=voltear(list(entrada),int(k))
	
	if result==-1:
		print("Case #"+str(x+1)+": IMPOSSIBLE")
	else:
		print("Case #"+str(x+1)+": "+str(result))
