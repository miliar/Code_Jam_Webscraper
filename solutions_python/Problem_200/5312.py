def isTidy(n):
	if(n[-1]==0):
		return False
	else:
		for i in range(len(n)-1,0,-1):
			if(n[i]>=n[i-1]):
				continue
			else:
				return False
		return True

t = int(input())

for i in range(t):
	a = input()
	for j in range(int(a),0,-1):
		if isTidy(str(j)):
			print("Case #{}: {}".format(i+1, j))
			break;