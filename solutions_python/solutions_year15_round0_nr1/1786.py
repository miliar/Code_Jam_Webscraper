import time
start = time.time();

# Open input and output file
in_file = open("input","r")
out_file = open("output","w")

T = int(in_file.readline())
print "T: " + str(T)

# Parse all test cases
t = 1
while (t <= T):
	in_line = in_file.readline()
	in_tokens = in_line.split()	
	S_max = int(in_tokens[0])
	crowd = in_tokens[1]
	
	# Parse all spectators 
	s = 1
	total_friends = 0
	threshold = int(crowd[0])
	while (s <= S_max):
		if(threshold >= s):
			threshold = threshold + int(crowd[s])
			s = s + 1
		else:
			friends = s - threshold
			total_friends = total_friends + friends
			threshold = threshold + friends + int(crowd[s])
			s = s + 1

			
	# Save test case output 
	print "Case #" + str(t) + ":" + " " + str(total_friends)
	out_file.write("Case #" + str(t) + ":" + " " + str(total_friends) + "\n")

	t = t + 1


# Close input and output 
in_file.close()
out_file.close()

# Print elapsed time
end = time.time()
print "\n\n Executed in: " + str(end - start)