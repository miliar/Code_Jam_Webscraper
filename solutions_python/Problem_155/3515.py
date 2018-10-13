def solution(max_shyness, audience):
	added = 0
	clapping = 0	
	for shyness, persons in enumerate(audience):
		if persons == 0: continue
		
		required_to_clap = shyness - clapping
		
		if required_to_clap > 0:
			added += required_to_clap
			clapping += added
			
			if added > max_shyness: break
	
		clapping += persons
		
	return added


if __name__ == "__main__":
	test_cases = input()
     
	for case in xrange(1, test_cases + 1):
		a,b = raw_input().split() 
	
		max_shyness = int(a)
		audience = map(int, list(b))
		
		print "Case #%i: %s" %  (case, solution(max_shyness, audience))


#4
#4 11111
#1 09
#5 110011
#0 1

#Case #1: 0
#Case #2: 1
#Case #3: 2
#Case #4: 0
