import sys

oF =  open(sys.argv[1],'r')
T = int(oF.readline())

for i in range(T):
	info = [int(x) for x in oF.readline().strip().split()]
	N  = info[0]
	S = info[1]
	P = info[2]
	scores = info[3:3+N]
	min_score = 3*P-2
	min_sur_score = 3*P-4


	count = 0
	s_count  = 0
	for score in scores:
		if score == 0:
			if P == 0:
				count=count+1
				continue
			else:
				continue
		if score >= min_score:
			count=count+1
		elif score>=min_sur_score:
			s_count=s_count+1

	if s_count>=S:
		count=count+S
	else:
		count=count+s_count
	print 'Case #%d: %d'%(i+1,count)
	
