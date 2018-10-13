import sys;
import math;
import fractions

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for case in range(T):
	input = map(int, f_ip.readline().split());
	
	gcd = fractions.gcd(input[1],100);
	if (100/gcd) > input[0]:
			print "Case #" + str(case+1) + ":",
			print "Broken"
	else:
		if input[2] == 0 or input[2] == 100:
			if (input[2] == input[1]):
				print "Case #" + str(case+1) + ":",
				print "Possible"
			else:
				print "Case #" + str(case+1) + ":",
				print "Broken"
		else:
			print "Case #" + str(case+1) + ":",
			print "Possible"