def main():
	num_cases = int( raw_input() )
	
	for case in xrange(1, num_cases+1):
		first_ans, first_set = int( raw_input() ), set()
		
		for i in xrange(1, 5):
			line = raw_input()
			
			if i == first_ans:
				first_set.update( map(int, line.split()) )
				
		sec_ans, sec_set = int( raw_input() ), set()
		
		for j in xrange(1, 5):
			line = raw_input()
			
			if j == sec_ans:
				sec_set.update( map(int, line.split()) )
		
		final = first_set & sec_set
		num_final = len(final)
		
		msg = 'Case #' + str(case) + ': '
		
		if num_final == 0:
			msg += 'Volunteer cheated!'
		elif num_final > 1:
			msg += 'Bad magician!'
		else:
			for num in final:
				msg += str(num)
				
		print msg

if __name__ == "__main__":
	main()