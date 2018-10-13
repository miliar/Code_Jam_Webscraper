# David Mende
# Google Code Jam 2017
# Qualification Round
# Problem B

# Check whether number is tidy
def tidy(s):
	for a,b in zip(s,s[1:]):
		if a > b:
			return False
	return True

# Return greatest tidy number less than or equal to input
def tidynum(s):
	if tidy(s):
		return int(s)
	fst = 0
	for i in range(len(s)-1):
		if s[i] < s[i+1]:
			fst = i+1
		if s[i] > s[i+1]:
			return int(s[:fst]+str(int(s[fst])-1)+'9'*(len(s)-fst-1))

for i in range(int(input())):
	print('Case #'+str(i+1)+':',tidynum(input()))
