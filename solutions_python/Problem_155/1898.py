f = open("A-small-attempt0.in","r")
fo = open("op.txt","w")

total_test_case = int(f.readline().split("\n")[0])

for i in range(total_test_case):

	line = f.readline()

	splitted = line.split(' ')

	total_audience = int(splitted[0])

	s_level = str(splitted[1].split('\n')[0])

	need_to_invite = 0
	stood_up = 0

	for j in range(len(s_level)):
		if j == 0:
			stood_up += int(s_level[j])
		else:
			if int(s_level[j]) != 0: 
				if stood_up < j:
					need_to_invite += ( j - stood_up )
					stood_up += (need_to_invite+1)*int(s_level[j])
				else:
					stood_up += int(s_level[j])



	fo.write("Case #"+str(i+1)+": "+str(need_to_invite)+"\n")
	# print "Case #",
	# print int(i),
	# print ": ",
	# print need_to_invite
fo.close()




