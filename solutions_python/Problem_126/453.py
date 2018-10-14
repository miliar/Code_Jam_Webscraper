def process(st):
	result=[]
	for i in st:
		if i in ['a','e','i','o','u']:
			result.append('t')
	 	else:
			result.append('c')
	return ''.join(result)



def main():
	inpu=open("A-small-attempt0.in",'r')
	output=open("sample.out","w+")
	total=int(inpu.readline())

	for sequence in xrange(total):
		temp=inpu.readline().split(" ")
		name=temp[0]
		n=int(temp[1])
		match=['c' for t in xrange(n)]
		match="".join(match)
		name=process(name)
#		print "**",match,name
		total=0
		for x in xrange(len(name)-n+1):
			for y in xrange(x+n-1,len(name)):
#				print match, name[x:y+1]
				if match in name[x:y+1]:
					total+=1
#					print "yes"
		output.write("Case #%d: %d\n"%(sequence+1, total))
		print("Case #%d: %d\n"%(sequence+1, total))
		
main()