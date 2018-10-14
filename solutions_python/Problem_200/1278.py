t=int(input())
def valid(vals):
	for i in range(len(vals)-1):
		if vals[i]>vals[i+1]:
			return False
	return True
def tidy(vals):
	vec=vals[:]
	for i in range(len(vec)-1,0,-1):
		if vec[i]<vec[i-1]:
			vec[i-1]-=1
			for j in range(i,len(vec)):
				vec[j]=9
	return int("".join(map(str,vec)))
for i in range(t):
	strin=input()
	vals=list(map(int,list(strin)))
	if valid(vals):
		print("Case #{}: {}".format(i+1, strin))
	else:
		print("Case #{}: {}".format(i+1, tidy(vals)))