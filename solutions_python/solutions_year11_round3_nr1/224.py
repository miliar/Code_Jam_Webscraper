input = open("A-large.in").read().split("\n")


def red(a):
	n,m=len(a), len(a[0])
	for i in xrange(n-1):
		for j in xrange(m-1):
			if a[i][j]=='#':
				if a[i][j]=="#" and a[i][j+1]=="#" and a[i+1][j]=="#" and a[i+1][j+1]=="#":
					a[i][j],a[i][j+1]="/","\\"
					a[i+1][j],a[i+1][j+1]="\\","/"
				else:
					return False
	for i in xrange(n):
		if '#' in a[i]:
			return False
	return True
			

T = int(input[0])
output = []
line=1
for t in xrange(1,T+1):
	n,m = [int(x) for x in input[line].split()]
	line+=1
	a=[list(s) for s in input[line:line+n]]
	line+=n
	output.append("Case #"+str(t)+":")
	if not red(a):
		output.append("Impossible")
	else:
		for s in a:
			output.append("".join(s))
	
	
	
#print output
open("a.out","w").write("\n".join(output))