import sys;
import math;

ip_f = open(sys.argv[1], 'r')

T = int(ip_f.readline());

for i in range(T):
	(C,F,X) = list(map(float,ip_f.readline().split()))
	rate = 2;
	if X > C:
		min_rate_req = (X-C)*F/C;
		iterations = math.ceil((min_rate_req-rate)/F);
		time = 0;
		for j in range(iterations):
			time = time + (C/rate);
			rate = rate+F;
		time = time + (X/rate);
		print("Case #%d: %.7f" %(i+1,time));
	else:
		print("Case #%d: %.7f" %(i+1,X/rate));
	