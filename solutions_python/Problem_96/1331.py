filein = open(r'd:\in.txt')
all_text = 	filein.read()
lines = all_text.split('\n')
n = int(lines[0])
results = []
for i in range(1,n+1):
	digits = lines[i].split(" ")
	N = int(digits[0]) 
	s = int(digits[1])
	p = int(digits[2])
	score = []
	c1 = 0
	c2 = 0
	for j in range(0,N):
		score.append(int(digits[j+3]))
		print score[j],p,(p - 1)*3
		if(score[j] > (p - 1)*3 and score[j] >= p):
			c1+=1
		elif(score[j] >= (p-1)*3 - 1  and score[j] >= p):
			c2+=1
	results.append(c1+min(c2,s))
out = ''
for i in range(1,n+1):
	out += "Case #%d: %s\n"%(i,results[i-1])
fileout = open(r"d:\out.txt","w")
fileout.write(out)
fileout.close()	