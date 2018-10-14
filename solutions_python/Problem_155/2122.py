f = open("Large.in")
outf = open("ans.txt", "w")
lines = f.readlines()
l = int(lines[0])
answer = 0
curr = 0
for a in range(1,l+1):
	temp = lines[a]
	print temp
	s = temp.split(" ")
	if (a != l):
		s[1] = s[1][:-1]
	if (s[1].find('0')==-1): 
		answer = 0
	else:
		for b in range(0,len(s[1])):
			print str(b) + " " + s[1][b]
			if (b > curr): 
				answer += b-curr
				curr += b-curr
			print s[1][b]
			curr += int(s[1][b])


	curr = 0
	if (a!=l):
		outf.write("Case #" + str(a) + ": " + str(answer) +"\n")
	else:
		outf.write("Case #" + str(a) + ": " + str(answer))
	answer = 0
	