import sys,math



file = open("A-small.in", "r")
input = file.readlines()
output = open("output.txt", "w");
L, D, N = input[0].split(" ")
L = int(L)
D = int(D)
N = int(N)
words = []

for word in input[1:D+1]:
	words.append(word[:-1])
cases = input[D+1:]

openPar = False

casen = 1
for case in cases:
	token = ''
	tokens = []	
	for char in case:
		if char is '(':
			openPar = True
		elif char is ')':
			openPar = False
			if token is not '':
				tokens.append(token)
			token = ''
		elif openPar:
			token += char
		else:
			tokens.append(char)
		
	count = [0] * L
	total = 0
	
	for word in words:
		correct = True
		for i in range(L):
			if word[i] not in tokens[i]:
				correct = False
				break
						
		if correct:
			total+=1
	print total	
	output.write("Case #%d: %d\n" % (casen, total) )
	
	casen += 1
	

output.close()
file.close()


	

