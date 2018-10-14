filename = "input_files/"
#filename += "in.in"
filename += "A-large.in"
#filename += ".out"
with open(filename) as f:
	trials = int(f.readline())
	#print(trials)
	for i in range(0,trials):
		s_max, audience_raw = f.readline().split(' ')
		s_max = int(s_max)
		audience_raw = list(audience_raw)
		audience_raw.remove("\n")
		
		audience_raw = [ int(s) for s in audience_raw]
		audience = [0] * (s_max+1)
		#print("S_max: ", s_max)
		#print(audience)
		used = 0
		for index, num in enumerate(audience_raw):
			if (num > 0):
				used += 1;
				audience[index] = num
		#print(audience)
		#print("S_max: ", s_max)
		
		sum = audience[0]
		num_invite = 0
		for x in range(1,len(audience)):
			if (sum < x):
				num_invite += 1
				sum += 1
			sum += audience[x]
			#print (x, audience[x], sum, num_invite)
			
		print("Case #" + str(i+1) + ": " + str(num_invite))
				
		
		
		
		
	
