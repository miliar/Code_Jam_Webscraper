import sys,math

filename = sys.argv[1]
f = open(filename, 'r')

for i in range(int(f.readline().strip())):
	seq = f.readline().strip().split()
	time = 0
	b_loc = 1
	o_loc = 1
	prev_bot = seq[1]
	b_time = 0
	o_time = 0
	for j in range(1,len(seq)):
		if j%2 == 1:
			if seq[j]=='B':
				c_time = int(math.fabs(b_loc-int(seq[j+1])))+1
				if prev_bot == 'B':
					b_time += int(math.fabs(b_loc-int(seq[j+1])))+1
					time += int(math.fabs(b_loc-int(seq[j+1])))+1
				elif o_time >= c_time:
					b_time=1
					time+=1
				elif o_time < c_time:
					b_time=c_time-o_time
					time+=c_time-o_time
				b_loc=int(seq[j+1])
				prev_bot = 'B'
			
			else:
				c_time = int(math.fabs(o_loc-int(seq[j+1])))+1
				if prev_bot == 'O':
					o_time += int(math.fabs(o_loc-int(seq[j+1])))+1
					time+=int(math.fabs(o_loc-int(seq[j+1])))+1
				elif b_time >= c_time:
					o_time=1
					time+=1
				elif b_time < c_time:
					o_time=c_time-b_time
					time+= c_time-b_time
				o_loc=int(seq[j+1])
				prev_bot = 'O'

					
	print 'Case #'+str(i+1)+':',time