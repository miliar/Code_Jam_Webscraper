def GCD(x,y):
	if(x<y):
		return GCD(y,x)
	elif(y == 0):
		return x
	elif(x%y == 0):
		return y
	else:
		return GCD(y,x%y)
		
T = int(raw_input())
for i in range(T):
	str_input = raw_input().split(' ')
	N = int(str_input[0])
	PD = int(str_input[1])
	PG = int(str_input[2])
	#print N,PD,PG
	gcd_pd = GCD(PD,100)
	gcd_pg = GCD(PG,100)
	day_stat = [100/gcd_pd,PD/gcd_pd,100/gcd_pd-PD/gcd_pd]
	all_stat = [100/gcd_pg,PG/gcd_pg,100/gcd_pg-PG/gcd_pg]
	if(day_stat[0] > N):
		print "Case #" + str(i+1) + ": Broken"
		continue
	if(day_stat[0] <= all_stat[0] and day_stat[1] <= all_stat[1] and day_stat[2] <= all_stat[2]):
		print "Case #" + str(i+1) + ": Possible"
		continue
	max_mul = max(day_stat)
	all_stat[0] *= max_mul
	all_stat[1] *= max_mul
	all_stat[2] *= max_mul
	#print all_stat
	if(day_stat[0] <= all_stat[0] and day_stat[1] <= all_stat[1] and day_stat[2] <= all_stat[2]):
		print "Case #" + str(i+1) + ": Possible"
		continue
	print "Case #" + str(i+1) + ": Broken"
	continue
	
	
