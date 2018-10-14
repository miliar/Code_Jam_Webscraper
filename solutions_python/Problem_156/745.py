s = [item.rstrip('\n') for item in open('text.txt','r').readlines()]



def main(n):
	

	n = nom(n)
	n = sorted(n, reverse=True)

	
	min = n[0][0]
	br = 0
	while br < min and n[0][0] > 3:
		
		fin = (tots(n[0]))
		

		gu = fin - ((fin/(len(n[0])+1)) * (len(n[0])+1))

		n[0].append(fin/ (len(n[0]) +1))
		t = 0
		
		while t < len(n[0]):
			if t < gu:
				n[0][t] = fin/len(n[0]) + 1
			else:
				n[0][t] = fin/len(n[0])
			t += 1
			


		br = getLost(n)
		n = sorted(n, reverse=True)
		
		

		if n[0][0] + br < min:
			min = n[0][0] + br


			
		
		
			
	return min
				
				
def nom(n):
	for t in range(0,len(n)):
		n[t] = [int(n[t])]
	return n
	
def tots(y):
	x = 0
	for t in y:
		x += t
	return x
	


def getLost(n):
	br = 0
	for t in range(0,len(n)):
		n[t] = sorted(n[t], reverse=True)
		br += len(n[t]) - 1
	return br
		
	
	

		
		



text_file = open('Tout.txt', 'w')
c = 1
for t in range(0, int(s[0])):
	text_file.write("Case #" + str(t+1) + ": " + str(main(s[c+1].split())) + '\n')

	c += 2
text_file.close()