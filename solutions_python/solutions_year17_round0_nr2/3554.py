import sys

f = open(sys.argv[1])

lines = f.readlines()

f.close()

T = int(lines[0])

p = open(sys.argv[2], "w")

for i in range(1, T+1):
	N = int(lines[i])
	print "question: " + str(N)
	num = N+1
	N_string = str(N)
	last = int(N_string[-1])
	for q in range(len(N_string)-1, -1, -1):
		digit = int(N_string[q])
		#print digit
		if digit <= last:
			#print "less that or equal to last"
			last = digit
			continue
		elif digit > last:
			#print "more than last"
			N_string = N_string[:q] + str(digit-1) + "9"*len(N_string[q+1:])
			last = digit-1
	p.write("Case #" + str(i) + ": " + str(int(N_string)) + "\n")	
	print "Case #" + str(i) + ": " + str(int(N_string))

p.close()	
		
