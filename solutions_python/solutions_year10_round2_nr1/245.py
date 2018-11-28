lines = open("A-large.in").read().split("\n")
output = []	
T = int(lines[0])
line_index = 1
for i in xrange(1, T+1):	
	n1, n2 = [int(x) for  x in lines[line_index].split()]
	line_index += 1
	
	old_dirs = []
	for k in xrange(n1):
		old_dirs.append( lines[line_index] )
		line_index +=1
		
	new_dirs = []
	for k in xrange(n2):
		new_dirs.append( lines[line_index] )
		line_index +=1
	
	dir_created = {}	
	root = "/"
	
	for s in old_dirs:
		p = s.split("/")[1:]
		for k in xrange(1, len(p)+1):
			dir_created[root+"/".join(p[:k])] = True
	
	r = 0
	for s in new_dirs:
		p = s.split("/")[1:]		
		for k in xrange(1, len(p)+1):
			 if not dir_created.get(root+"/".join(p[:k])):
				dir_created[root+"/".join(p[:k])] = True
				r += 1
	
	#print n1, n2
	#print old_dirs
	#print new_dirs
	result = "Case #"+str(i)+": "+ str(r)
	#print result
	
	output.append( result )
	
print "\n".join( output)
open("result.out", "w").write( "\n".join(output))