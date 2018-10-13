t_case = int(raw_input())
c_index = 1
while(t_case):
	e_a = 0
	s_o = 0
	s_string = str(raw_input())
	s_max, sl_string = s_string.split()
	s_o = int(sl_string[0])
	if s_o > s_max:
		print "Case #" + str(c_index) + ": " + str(e_a)
	else:
		for i in range(1, int(s_max) +1):
			if s_o >= i:
				s_o += int(sl_string[i])
			else:
				if int(sl_string[i]) != 0:
					e_a += i - s_o 
					s_o += int(sl_string[i]) + e_a
		print "Case #" + str(c_index) + ": " + str(e_a) 
	c_index += 1
	t_case -= 1