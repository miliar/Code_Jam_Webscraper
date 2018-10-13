def getcookies(c,f,x):
	#print(str(c)+" "+str(f)+" "+str(x))
	done=False
	rate=2
	numfarms=0
	cookies=0
	curtime=0
	while(not done):
		timetofarm=max(0, (c-cookies)/rate)
		#print("test")
		#print(cookies)
		#print(timetofarm)
		timeleftno=(x-cookies)/rate
		timeleftyes=timetofarm+(x-cookies)/(rate+f)
		#print(timeleftno)
		#print(timeleftyes)
		#print(cookies)
		#input()
		if (timeleftno>timeleftyes):
			numfarms=numfarms+1
			
			curtime=curtime+timetofarm
			#print("curtime="+str(curtime))
			cookies=cookies-c+rate*timetofarm
			rate=rate+f
		else:
			done=True
			curtime=curtime+timeleftno
	return curtime


f=open("input.txt","r")
o=open("output.txt", "w")
lines=f.readlines()
numinputs=int((lines[0]))
for i in range(1,numinputs+1):
	inputs=lines[i].split()
	o.write("Case #"+str(i)+": "+"{0:.7f}".format(getcookies(float(inputs[0]),float(inputs[1]),float(inputs[2])))+"\n")



