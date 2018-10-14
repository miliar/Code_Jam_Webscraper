def find_count(S,K):
	res = 0
	for i in range(len(S)-K+1):
		if S[i] == '-':
			res += 1
			temp = ['-']*K
			for j in range(0,K):
				if S[i+j] == '-':
					temp[j] = '+'
				else:
					temp[j] = '-'
			#print('temp:',temp)
			S = S[:i]+''.join(temp)+S[i+K:]
			#print('S:',S)
	for i in range(len(S)):
		if S[i] == '-':
			res = -1
			break
	return res
T = int(input())

for i in range(T):
	S,K = input().split()
	K = int(K)
	res = find_count(S,K)
	if res == -1:
		print('Case #'+str(i+1)+':','IMPOSSIBLE')
	else:
		print('Case #'+str(i+1)+':',res)
