def permutate(string):
	s = list(string)
	for index in range(len(s)):
		if s[index] == '-':
			s[index] = '+'
		else:
			s[index] = '-'
	return "".join(s)

probs = []

with open("A-large.in") as f:
	content = f.readlines()
content = [x.strip() for x in content] 

num_probs = int(content[0])

for i in range(1, num_probs+1):
	probs.append(content[i].split(" "))

for i in range(num_probs):
	count = 0
	perm = int(probs[i][1])
	string = probs[i][0]
	first = string.find('-')
	while first != -1 and first <= len(string) - perm:
		permutated = permutate(string[first:first+perm])
		string = string.replace(string[first:first+perm], permutated, 1)
		first = string.find('-')
		count += 1

	if string.find('-') == -1:
		print "Case #{}: {}".format(i+1, count)
	else:	
		print "Case #{}: IMPOSSIBLE".format(i+1)
