s = [item.rstrip('\n') for item in open('text.txt','r').readlines()]

def main(u):
	x = int(u[0])
	r = int(u[1])
	c = int(u[2])
	if c > r:
		lolo = r
		r = c
		c = lolo
		
	rc = (r,c)
	
	if (r * c) % x != 0 or (x > r and x > c):
		return "RICHARD"
		
	if x == 1:
		return "GABRIEL"
		
	if x == 4:
		if rc == (4, 2):
			return "RICHARD"
		if c == 1:
			return "RICHARD"
			
	if x == 3:
		if c == 1:
			return "RICHARD"
		
		
	

		
	return "GABRIEL"
	
	"""
	if x == 1:
		return "GABRIEL"
		
	if x == 2:
		return "GABRIEL"
		
	if x == 3
		return "GABRIEL"""
		
	
		
		
	
		





text_file = open('out.txt', 'w')
for t in range(1, int(s[0]) + 1):
	text_file.write("Case #" + str(t) + ": " + str(main(s[t].split())) + '\n')
text_file.close()