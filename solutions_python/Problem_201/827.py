
def get_empty_pair(s , p):
	b2len_s = len(bin(s))-2 
	b2len_p = len(bin(p))-2 

	# b2len_s_left = b2len_s - b2len_p 
	top_mask =  (1 << b2len_p) - 1 

	add_1_number = 1 << (b2len_p -1 )
	# print "add_1 ", bin(add_1_number)
	raw_result = s >> b2len_p 

	plen_s = top_mask & s
	# print "plen_s", bin(plen_s)

	if plen_s >= p : 
		return raw_result , raw_result
	elif (plen_s + add_1_number) >= p:
		return raw_result , raw_result -1 
	else :
		return raw_result -1 , raw_result -1 


if __name__ == '__main__' : 
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
	    	s ,p = raw_input().split()
		s = int (s) 
		p = int (p) 
		max_n , min_n = get_empty_pair(s, p )
	    	print "Case #%d: %d %d"%(i,max_n, min_n)
		         
