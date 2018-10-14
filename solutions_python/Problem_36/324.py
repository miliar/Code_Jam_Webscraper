#Welcome
string="welcome to code jam"
n=int(raw_input())
for s in xrange(n):
	word=raw_input()[::-1]
	numbers=[0]*len(string)
	numbers+=[1]
	for i in word:
		j=string.find(i)
		while (j!=-1):
			numbers[j]=(numbers[j]+numbers[j+1])%10000
			j=string.find(i,j+1)
	print "Case #"+str(s+1)+":",str(numbers[0]).rjust(4,"0")
			
	