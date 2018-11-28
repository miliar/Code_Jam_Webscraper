
f = open('1-large.in','r')
lines = f.readlines()
f.close()

n = int(lines[0])
output = ''
for i in range(n):
	
	char_list = []
	start_line = 5*i + 1
	win_flag = 0
		
	for j in range(4):		
		sorted_word = ''.join(sorted(lines[start_line+j]))
				
		if sorted_word.strip() == 'TXXX' or sorted_word.strip() == 'XXXX':
			output+= 'Case #' + str(i+1) + ': X won \n'
			win_flag = 1
			break
		elif sorted_word.strip() == 'OOOT' or sorted_word.strip() == 'OOOO':
			win_flag = 1
			output+='Case #' + str(i+1) + ': O won \n'	
			break
	
	if win_flag == 0:
		
		for j in range(4):
			word = lines[start_line][j] + lines[start_line+1][j] + lines[start_line+2][j] + lines[start_line+3][j] 
			sorted_word = ''.join(sorted(word))						
			
			if sorted_word.strip() == 'TXXX' or sorted_word.strip() == 'XXXX':
				output+='Case #' + str(i+1) + ': X won \n'
				win_flag = 1
				break
			elif sorted_word.strip() == 'OOOT' or sorted_word.strip() == 'OOOO':				
				win_flag = 1
				output+='Case #' + str(i+1) + ': O won \n'	
				break	
				
	if win_flag == 0:
		word = lines[start_line][0] + lines[start_line+1][1] + lines[start_line+2][2] + lines[start_line+3][3] 
		sorted_word = ''.join(sorted(word))
					
		if sorted_word.strip() == 'TXXX' or sorted_word.strip() == 'XXXX':
			output+='Case #' + str(i+1) + ': X won \n'
			win_flag = 1
			
		elif sorted_word.strip() == 'OOOT' or sorted_word.strip() == 'OOOO':				
			win_flag = 1
			output+='Case #' + str(i+1) + ': O won \n'	
					
	if win_flag == 0:
		word = lines[start_line][3] + lines[start_line+1][2] + lines[start_line+2][1] + lines[start_line+3][0] 
		sorted_word = ''.join(sorted(word))						
			
		if sorted_word.strip() == 'TXXX' or sorted_word.strip() == 'XXXX':
			output+='Case #' + str(i+1) + ': X won \n'
			win_flag = 1			
		
		elif sorted_word.strip() == 'OOOT' or sorted_word.strip() == 'OOOO':				
			win_flag = 1
			output+='Case #' + str(i+1) + ': O won \n'	
	
	if win_flag == 0:
		
		for j in range(4):
			word += lines[start_line + j] 
		
		if '.' in word:
			output+='Case #' + str(i+1) + ': Game has not completed \n'	
		else:
			output+='Case #' + str(i+1) + ': Draw \n'	

f = open('1.out','w')
f.write(output)
f.close()
