import sys

with open(sys.argv[1],'r') as f:
	t = int(f.readline().strip());
	for i in range(0,t):
		sup=0;
		count=0;
		values = f.readline().strip().split();
		p = int(values[2]);
		s = int(values[1]);
		for score in values[3:]:
			m = (2+int(score))/3;
			if m >= p:
				count+=1;
			elif m == (p-1) and int(score)%3 != 1 and int(score)>1:
				sup+=1;
#		print count;
 		count+=min(sup,s);
# 		print p,s, sup, count
 		print "Case #%d: %d"%(i+1,count);
 		
 		


