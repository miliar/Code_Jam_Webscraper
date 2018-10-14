import re

for case in range(input()):
	l = int(raw_input())
	tree = ""
	for i in xrange(l):
		tree += raw_input()
	a = int(raw_input())
	animals = []
	for i in xrange(a):
		data = raw_input().split(' ')
		animals.append(data[2 : ])
	print 'Case #%s:' % (case + 1)

	for animal in animals:
	
		cur = 0
		p = 1.0
		
		while tree[cur] != '(':
			cur += 1
		cur += 1	
			
		while True:
			r = re.compile('\s*(\d\.[\d]+)\s*\)').match(tree[cur: ])
			if r:			
				g = r.groups()
				p *= float(g[0])
				break
				
			r = re.compile('\s*(\d\.[\d]+)\s*([a-z]+)\s*\(').match(tree[cur: ])
			if r:			
				g = r.groups()
				p *= float(g[0])
					
			while tree[cur] != '(':
				cur += 1
				
#			print tree[cur: ]	
			
			if g[1] in animal:
				cur += 1	
				continue
			else:
				open_s = 1
				close_s = 0
				while open_s != close_s:
					cur += 1	
					if tree[cur] == '(':
						open_s += 1
					if tree[cur] == ')':
						close_s += 1
				while tree[cur] != '(':
					cur += 1
				cur += 1	

		print '%8f' % p									
					
					
				
				
						
					
					
	
				
				
			
				
	
		    
       	

