def flip_it_right(s,K,num):
	
	check = '+'*len(s)
	num =int(num)
	
	if check==s:	
		return str(num)
	elif len(s) < K and s != check:
			return 'IMPOSSIBLE'
	else:
		S = list(s)
		if S[0] == '-':
			for i in range(0,K):
				if S[i] == '+':
					S[i] = '-'
				elif S[i] == '-':
					S[i] = '+'
			num = num+1
		if S[-1] == '-':
			for i in range(len(S)-K,len(S)):
				if S[i] == '+':
					S[i] = '-'
				elif S[i] == '-':
					S[i] = '+'
			num = num+1
		s = "".join(S)
		s=s.lstrip('+')
		s=s.rstrip('+')
		return flip_it_right(s,K,str(num))

def flip(line, num):
	fields = line.split()
	K = int(fields[1])
	S = fields[0]
	if S == '-':
		return str(1)
	else:
		return flip_it_right(S,K,num)

fileName = 'A-large.in'
fileHandle =open(fileName, 'r')
firstLine = fileHandle.readline().rstrip()
numTests = int(firstLine)
k=1
for line in fileHandle:
	num = flip(line,0)
	print "Case #"+str(k)+": "+ num
	k=k+1


