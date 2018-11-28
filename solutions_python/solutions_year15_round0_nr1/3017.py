
def compute():
	count = 0
	
	if S[0] == 0:
		count+=1
		temp_sum = count
	else:	
		temp_sum = S[0]
	
	for i in range(1,S_MAX+1):
		if temp_sum < i and S[i] != 0:
			count += (i - temp_sum)
			temp_sum += (i - temp_sum + S[i])
		else:	
			temp_sum += S[i]
			
	print("Case #%d: %d" %(C,count))		


			

T = int(input())
C = 1
while T>0:
	S_MAX, S = input().strip().split(" ")
	S_MAX = int(S_MAX)
	S = list(map(int,list(S)))
	
	compute()
	T-=1
	C+=1
	