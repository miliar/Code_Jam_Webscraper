import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	tcCount=int(f.readline())
	# for each test case
	for n in range(tcCount):
		a = f.readline()
		a= a.split()
		a= map(int, a)
		p = a[0]
		k=a[1]
		l=a[2]
		freq = f.readline()
		freq = freq.split()
		freq = map(int, freq)
		freq.sort()
		freq.reverse()
		assign = []
		for j in range(k):
			assign.append([])
		
		while (len(freq) > 0):
			for j in range(k):
				if (len(freq) == 0):
					break
				alpha = freq.pop(0)
				if len(assign[j]) < p:
					assign[j].append(alpha)
				
	
		cnt = 0
		for j in range(k):
			l = assign[j]
			for k in range(len(l)):
				cnt = cnt + (l[k]*(k+1))
		
		
		answer = cnt
		# Print the output
		outline = 'Case #'+str(n+1)+': '+str(answer)
		print outline
		outf.write(outline+'\n')

	f.close()
	outf.close()

main()