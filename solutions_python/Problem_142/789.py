t = int(raw_input())
for i in range(1,t+1):
	print "Case #%d:" %i,
	n = int(raw_input())
	words = []
	for j in range(n):
		x = raw_input()
		x = x+'2'
		words.append(x)
	j,k = 0,0
	ans = 0
	while True:
		if words[0][j] == '2' and words[1][k] == '2':
			break
		if words[0][j] == words[1][k]:
			j += 1
			k += 1
			continue
		else:
			if j>0 and k>0 and words[0][j-1] == words[0][j]:
				ans += 1
				j += 1
			elif j>0 and k>0 and words[1][k-1] == words[1][k]:
				ans += 1
				k += 1
			else:
				print "Fegla Won"
				ans = -1
				break
	if ans != -1:
		print ans



