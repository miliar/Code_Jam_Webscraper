import time
import math
start = time.time();

# Open input and output file
in_file = open("input","r")
out_file = open("output","w")

T = int(in_file.readline())
print "T: " + str(T)

# Parse all test cases
t = 1
while (t <= T):
	in_line = in_file.readline().split()
	X = int(in_line[0])
	R = int(in_line[1])
	C = int(in_line[2])

	if ( ((R*C) % X) != 0 ):
		winner = "RICHARD"
	elif (R < X and C < X):			
		winner = "RICHARD"
	elif (math.floor(X/2) > R or math.floor(X/2) >	C):
		winner = "RICHARD"
	elif (X == C and (X-R)==2):			
		winner = "RICHARD"	
	elif (X == R and (X-C)==2):			
		winner = "RICHARD"	
	elif ( X >= 7):			
		winner = "RICHARD"
	else:
		winner = "GABRIEL"
			
			
	# Save test case output 
	print "Case #" + str(t) + ":" + " " + winner
	out_file.write("Case #" + str(t) + ":" + " " + winner + "\n")

	t = t + 1


# Close input and output 
in_file.close()
out_file.close()

# Print elapsed time
end = time.time()
print "\n\n Executed in: " + str(end - start)