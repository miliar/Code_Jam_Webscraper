def main():
	input=open("B-large.in",'r')
#	input=open("C-small-attempt0.in",'r')
	output=open("B-large.out","w")
	total=int(input.readline())
	for i in range(0,total):
#		read in size
		size=input.readline().split(" ")
		m=int(size[0])
		n=int(size[1])
		a=[[] for b in range(m)]
		result=""
#		read in and fill in a
		for x in range(m):
			line=input.readline().split(" ")
			for y in range(n):
#				print line[y],
				a[x].append(int(line[y]))
		
#		Judge:
		for x in range(m):
			for y in range(n):
				#check vertical have higher
				for c in range(m):
					if a[c][y]>a[x][y]:
						#check horizontal have higher
						for d in range(n):
							if a[x][d]>a[x][y]:
								result="NO"
								
		if result=='':
			result="YES"
		print "Case #:%d %s"%(i+1, result)
		output.write("Case #%d: %s\n"%(i+1, result))

main()