# David Mende
# Google Code Jam 2017
# Qualification Round
# Problem A

# Of all n-k+1 possible flips, no flip should ever be repeated,
#	so let each flip be a variable modulo 2
# System of n linear equations modulo 2 determines unique solution,
# 	but since there are more equations than variables, there might
#	not always be a valid solution
# The greedy approach always discovers this solution if it exists

# Find minimum number of flips necessary
def minflips(s,k):
	n = len(s)
	t = [1 if a == '+' else 0 for a in s]
	count = 0
	for i in range(n-k+1):
		if t[i] == 0:
			count += 1
			for j in range(k):
				t[i+j] = 1 - t[i+j]
	return count if 0 not in t else 'IMPOSSIBLE'

for i in range(int(input())):
	s,k = input().split()
	k = int(k)
	print('Case #'+str(i+1)+':',minflips(s,k))
