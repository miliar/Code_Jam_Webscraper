# python 2

infile = open("B-small-attempt1.in","r")
outfile = open("B-small-output.out","w")

t = int(infile.readline())

def isTidy(n):
	if n < 10:
		return True
	elif n%10 < (n/10)%10:
		return False
	else:
		return isTidy(n/10)

for i in range(t):

	num = int(infile.readline())

	y = isTidy(num)

	while(y != True):

		if isTidy(num - num/10) and len(str(num)) > 3:
			num = num - num/10
			break

		if num%10 == 0:
			num = num - 1
		else:
			num = num - num%10

		y = isTidy(num)

	#print num
	outfile.write("Case #"+str(i+1) +": "+ str(num)+"\n")

infile.close()
outfile.close()
