import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	tcCount=int(f.readline())
	# for each test case
	for i in range(tcCount):
		vcount = int(f.readline())
		v1 = f.readline()
		v1 = v1.split()
		v1 = map(int, v1)
		v2 = f.readline()
		v2 = v2.split()
		v2 = map(int, v2)
		v1.sort()
		v2.sort()
		v2.reverse()
		
		answer = scalar(v1,v2)
		# Print the output
		outline = 'Case #'+str(i+1)+': '+str(answer)
		print outline
		outf.write(outline+'\n')

	f.close()
	outf.close()

def scalar(x, y):
	sum = 0
	
	for i in range(len(x)):
		sum = sum + (x[i] * y[i])
	return sum
main()