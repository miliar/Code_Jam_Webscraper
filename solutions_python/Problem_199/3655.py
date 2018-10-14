testcase = input("")
#print type(testcase)
with open("in.txt", "r") as xt:
    topwrds_list = xt.read().split("\n")
   # testcase=topwrds_list[0]
for l in range(testcase):
	#string1,k = raw_input("").split(" ")
	#print topwrds_list
	string1,k = topwrds_list[l+1].split(" ")
	k = int(k)
	count = 0
	flag= "0"
	string=list(string1)
	#print string+" "+str(k)
	for i in range(len(string)-k+1):
		#print str(string)
		if(string[i]=="-"):
			count = count+1
			for p in range(k):
				#if((i+p)>len(string)):
					#break
				#else:
					if(string[p+i]=="+"):
						string[i+p]="-"
					else:
						string[i+p]="+"
	for i in range(len(string)):
		if(string[i]=="-"):
			print "Case #"+str(l+1)+": IMPOSSIBLE"
			flag = "1"
			break
	#print str(string)
	if(flag=="0"):
		print "Case #"+str(l+1)+": "+str(count)

