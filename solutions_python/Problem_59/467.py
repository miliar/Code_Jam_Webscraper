from sys import stdin

def sol():
	str_dir = []
	str_mkdir = []
	have_dir = []
	mkdir = []
	dir = []
	count=0;
	
	created, create = [int(x) for x in stdin.readline().split(' ')]
	for hd in range(created):
		str_dir.append(stdin.readline().strip())
	for mk in range(create):
		str_mkdir.append(stdin.readline().strip())
	
	for a in str_dir:
		have_dir.append(a.split('/'))
	for b in str_mkdir:
		mkdir.append(b.split('/'))
	
	#print have_dir
	#print mkdir
	
	for n in have_dir:
		prev = ""
		i=-1
		for m in n:
			i+=1
			if i==1 and m is not '' and ([m,i] not in dir) :	
				dir.append([m,i])
			if i>1 and m is not '' and ([m,i,prev] not in dir) :	
				dir.append([m,i,prev])
			if m is not '':
				prev += "/" + m
			
	
	for n in mkdir:
		prev = ""
		i=-1
		for m in n:
			i+=1
			if i==1 and m is not '' and ([m,i] not in dir) :	
				dir.append([m,i])
				count+=1
			if i>1 and m is not '' and ([m,i,prev] not in dir) :	
				dir.append([m,i,prev])
				count+=1
			if m is not '':
				prev += "/" + m
	print 'Case #%d:' % (case+1),count
	#print dir
	
num = int(stdin.readline())
for case in range(num):
	#print 'Case #%d:' % (case+1), 
	sol()
