from sys import stdin, stdout
cin=open("in")
cout=open("out","w")
n_cases=int(cin.readline().rstrip())

#Represent times as tuples.
ordering_dict={"ready": 0, "depart": 1}
#Ensures that for simutaneous events a train being ready is done before one has to depart
def ordering(m,n):
	if m[0]!=n[0]:
		return cmp(m[0],n[0])
	if m[1]!=n[1]:
		return cmp(m[1],n[1])
	return cmp(ordering_dict[m[3]],ordering_dict[n[3]])

def minSec(string_rep):
	return map(int, string_rep.split(":"))

def addMins(t, n_mins):
	tmp=t[1]+n_mins
	return (t[0]+tmp/60, tmp%60)

for case_i in xrange(1,n_cases+1):
	print "New Case"		
	turn=int(cin.readline().rstrip())
	(from_a, from_b)=map(int, cin.readline().split())
	events=[]
	for i in range(from_a+from_b):
		(depart, arrive)=map(minSec, cin.readline().split())
		if i<from_a:
			depart_loc=0
			arrive_loc=1
		else:
			depart_loc=1
			arrive_loc=0
		events.append((depart[0],depart[1],depart_loc,"depart"))
		ready_time=addMins(arrive, turn)
		events.append((ready_time[0],ready_time[1],arrive_loc,"ready"))
	events.sort(cmp=ordering)
	#Trains for at the start	
	trains_ini=[0,0]
	#Trains available now
	trains_now=[0,0]
	locations=["a","b"]
	for e in events:
		loc=e[2]
		print e,
		if e[3]=="depart":
			if trains_now[loc]>0:
				print ": deploy ready train ", locations[loc]
				trains_now[loc]-=1
			else:
				print ": deploy new train ", locations[loc]
				trains_ini[loc]+=1
		else:
			#=="ready"
			print " train now ready ", locations[loc]
			trains_now[loc]+=1
	cout.write("Case #"+str(case_i)+": "+str(trains_ini[0])+" "+str(trains_ini[1])+"\n")

