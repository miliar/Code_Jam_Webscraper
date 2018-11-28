def swap_di(thing,total_len,need_len):
	thing_list=[]
	temp3=[]
	i=0
	for das in thing:
		thing_list.append(das)
		temp3.append(das)
	for x in range(total_len-need_len+1,total_len+1):
		temp3[i]=thing_list[x]
		i+=1
	for x in range(0,total_len-need_len+1):
		temp3[i]=thing_list[x]
		i+=1
		stuff=""
		for das in temp3:
			stuff+=das
	return stuff
#################################
f_in = open('/home/anirudh/codejam/p3/q2_input', 'r')
f_out = open('/home/anirudh/codejam/p3/q2_output', 'w')

num = int(f_in.readline())
for x in range(num):
	line = f_in.readline()
############################################################porb-starts###########################################
	Maj_count = 0
	import shlex
	pebbles = shlex.split(line)
	Upper_limit = int(pebbles[1])
	Lower_limit = int(pebbles[0])
	len1=len(str(Lower_limit))
	for stuff in range(Lower_limit,Upper_limit+1):
		for dip in range(1,len1):
			stuff2=swap_di(str(stuff),len1-1,dip)
			if Lower_limit <= int(stuff) and int(stuff) < int(stuff2) and int(stuff2) <= Upper_limit:
#				f_out.write(str(Lower_limit)+" <= "+stuff+" < "+stuff2+" <= "+str(Upper_limit))
#				print str(Lower_limit)+" <= "+str(stuff)+" < "+str(stuff2)+" <= "+str(Upper_limit)
				Maj_count+=1
#	print "Case #"+str(x)+": "+str(Maj_count)
	f_out.write("Case #"+str(x+1)+": "+str(Maj_count))
	f_out.write("\n")
############################################################porb-ends###########################################

