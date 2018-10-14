N = int(raw_input())

for n in range(N):
	k = int(raw_input())
		
	for i in range(4):
		t = raw_input()
		
		if(i+1 == k): 
			a = map(int, t.split())
			
	k = int(raw_input())
	for i in range(4):
		t = raw_input()
		
		if(i+1 == k): 
			b = map(int, t.split())
		
	x = [val for val in a if val in b]
			
	if len(x)  > 1:
		res = 'Bad magician!'
	elif len(x) == 0:
		res = 'Volunteer cheated!'		
	elif len(x) == 1:
		res = x[0]
	
	print 'Case #%d: %s' % (n+1, res)
	
	