# Google Codejam 2008
# Train Timetable

def convert_time(str):
	a,b = str.split(":")
	return int(a)*60 + int(b)

def input_time(str,x): # x denotes state
	a,b = str.split()
	return [convert_time(a),convert_time(b),x]

for case in range(input()):
	t = input()
	na,nb = map(int,raw_input().split())
	time = []
	exist = [1]*(na+nb)
	for i in range(na):
		time.append(input_time(raw_input(),0))
	for i in range(nb):
		time.append(input_time(raw_input(),1))

	time.sort()
	nt = [0,0]
	for i in range(len(time)):
		if exist[i]==0: continue
		ctime,next = time[i][1]+t, not time[i][2]
		nt[time[i][2]] = nt[time[i][2]] + 1
		exist[i] = 0
		if i==len(time)-1: continue
		for j in range(i+1,len(time)):
			if time[j][0]>=ctime and exist[j]==1 and time[j][2]==next:
				exist[j] = 0
				ctime = time[j][1]+t
				next = not next
	
	print "Case #%s: %s %s" % (case+1,nt[0],nt[1]) 
	
	