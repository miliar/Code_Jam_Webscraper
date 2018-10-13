import fractions
import sys
sys.setrecursionlimit(3000)

		
def extgcd(myls):
	if len(myls) <= 0:
		print("Yahoo!")
		return 0
	elif len(myls) == 1:
		return myls[0]
	else:
		k = fractions.gcd(myls[0],myls[1])
		if (len(myls) == 2):
			return k
		if (k == 1):
			return k
		return extgcd([k]+myls[2:])
def dap(myls):
	k = min(myls)
	t = [(p-k) for p in myls]
	t.remove(0)
	thegcd = extgcd(t)	
	if (k%thegcd == 0):
		return 0
	else:
		return (thegcd - (k%thegcd))

myin = open("b.in")
myout = open("b.out","w")
inputnum = int(myin.readline().strip())
for k in range(1,inputnum+1):
	p = myin.readline().strip().split()
	numb = [int(t) for t in p[1:]]
	theans = dap(numb)
	myout.write("Case #")
	myout.write(str(k))
	myout.write(": ")
	myout.write(str(theans))
	myout.write("\n")



