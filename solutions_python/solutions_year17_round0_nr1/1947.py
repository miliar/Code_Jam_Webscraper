def flip(pancake):
	if pancake == '+':
		return '-'
	else:
		return '+'
		

T = int(input())

for t in range(1, T + 1):
	line = input().split(" ")
	S = line[0].strip("+")
	K = int(line[1])
	
	moves = 0
	while K <= len(S):
		S = ('').join([flip(S[i]) if i < K else S[i] for i in range(len(S))])
		S = S.strip("+")
		moves += 1
	
	
	print("Case #{}: {}".format(t, moves if len(S) == 0 else "IMPOSSIBLE"))