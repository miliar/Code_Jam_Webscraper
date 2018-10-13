T = int(input())
for I in range(1, T+1):
	N = int(input())
	strings = []
	for i in range(0, N):
		strings.append(input())
	
	chars = []
	for s in strings:
		res = []
		tmp = [s[0], 1]
		for i in range(1, len(s)):
			if s[i] == tmp[0]:
				tmp[1] += 1
			else:
				res.append(tmp)
				tmp = [s[i], 1]
		res.append(tmp)
		chars.append(res)
	
	possible = True
	length = len(chars[0])
	for i in chars:
		if len(i) != length:
			possible = False
			break
	
	#print (chars)
	#print("############")
	result = 0
	if possible:
		for i in range(0, len(chars[0])):
			if not possible:
				break
			ave = 0
			curr = chars[0][i][0]
			for j in range(0, len(chars)):
				if chars[j][i][0] != curr:
					possible = False
					break
				else:
					ave += chars[j][i][1]
			ave = round((ave*1.0)/(len(chars)*1.0))
			for j in range(0, len(chars)):
				result += abs(ave - chars[j][i][1])
	
	if not possible:
		print("Case #%d: Fegla Won" % (I))
	else:
		print("Case #%d: %d" % (I, result))
		
	