out = []
def NumberCheck(n):
	global out
	a = n%10
	n = n//10
	if n==0:
		out.append(a)
		return
	b = n%10
	
	if a==9:
		out.append(a)
		NumberCheck(n)
	elif a<b:
		out.append(9)
		for i in range(len(out)-1):
			if out[i]<9:
				out[i]=9
		NumberCheck(n-1)
	else:
		out.append(a)
		NumberCheck(n)
		


with open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/TidyNumbers/B-large.txt') as f:
	a = []
	for line in f:
		a.append(line)
		
fout = open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/TidyNumbers/B-largeOut1.txt', 'w')
		
N = int(a[0][0])
case = 1

A = []
for i in range(1,len(a)):
	A.append(int(a[i]))


for i in range(len(A)):
	NumberCheck(A[i])
	out1 = ''
	if out[len(out)-1] == 0:
		out = out[0:len(out)-1]
	for i in range(len(out)-1):
		if out[i]<out[i+1]:
			out[i] = out[i+1]
	for i in range(len(out)):
		out1+=str(out[len(out)-i-1])
	out1+='\n'
	fout.write("Case #" + str(case) + ": " + out1)
	case += 1
	out = []
