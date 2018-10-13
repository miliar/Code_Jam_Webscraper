f = open('C:\\Users\\narayv@amazon.com\\Desktop\\CodeJam\\Prob_B\\B-large.in', 'r')
output = open('C:\\Users\\narayv@amazon.com\\Desktop\\CodeJam\\Prob_B\\output_b.txt', 'w')
N_O_T = int(f.readline())
i = 0

while i < N_O_T :
	
	config = [float(p) for p in f.readline().split()]
	C = float(config[0]) # Cost of Cookie Farm
	F = float(config[1]) # Extra Cookies per second gained for additional farm
	X = float(config[2]) # Cookies to win
	total_t = 0			 # Total Time
	cr_rate = float(2)   # 2 cookies per second
	t_new_rate = 0
	t_cr_rate = 1
	
	while t_new_rate < t_cr_rate :
		t_cr_rate = X/cr_rate						# Time with current rate
		t_new_rate = (X/(cr_rate + F)) + (C/cr_rate) # Time with new rate
		
		#print t_cr_rate
		#print t_new_rate
		#raw_input()

		if t_new_rate < t_cr_rate :
			total_t = total_t + (C/cr_rate)
		else :
			total_t = total_t + (X/cr_rate)
		#print total_t
		cr_rate = cr_rate + F
		#print cr_rate
		#raw_input()
	#print round(total_t,7)
	output.write("Case #" + str(i+1) + ": " + str(round(total_t,7)) + "\n")
	#output.write(total_t)
	i = i + 1