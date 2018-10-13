fin = open("A-large.in","r")
fread = fin.readline
#fread = input
fout = open("A-large-output.out","w")

def main(tcase):
	d,n = [int(inpNum) for inpNum in fread().strip().split()]
	a = [[int(inpNum) for inpNum in fread().strip().split()] for i in range(n)]
	mxTime = 0
	for i in a:
		mxTime = max(mxTime,(d-i[0])/i[1])
	print("Case #%d: %.7f"%(tcase,d/mxTime),file=fout)

for t in range(int(fread().strip())):
	main(t+1)

fout.close()
fin.close()