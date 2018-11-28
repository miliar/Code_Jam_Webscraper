def xundo(pattern):
	full = True
	for char in ['X','O']:
		winner3 = True
		winner4 = True
		for i in range(4):
			if pattern[i][i]!= 'T' and pattern[i][i]!= char:
				
				winner3 = False
			if pattern[3-i][i]!= 'T' and pattern[3-i][i]!=char:
				winner4 = False

			winner1 = True
			winner2 = True
			for j in range(4):
				if pattern[i][j]=='.':
					full = False

				if pattern[i][j]!= 'T' and pattern[i][j]!= char:
					winner1 = False
				if pattern[j][i]!= 'T' and pattern[j][i]!= char:
					winner2 = False
			
			if(winner1 or winner2):
				return char+" won"
		if(winner3 or winner4):
			return char+" won"
	if(full):
		return 'Draw'
	return 'Game has not completed'


with open('A-large.in') as f:
    lines = f.read().splitlines()
    T = int(lines[0])
 
    line = 1
    for i in range(T):
    	pattern = []
    	for j in range(4):
    		pattern.append(lines[line])
    		line = line +1
    	print "Case #"+str(i+1)+": "+xundo(pattern)
    	line = line +1
