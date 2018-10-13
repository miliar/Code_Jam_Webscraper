
import fileinput


for index,line in enumerate(fileinput.input()):
	if index == 0:
		continue
	else:
		string = line.split(' ')[1]
		num_people_standing =  0
		need_to_invite = 0
		string = string.rstrip()
		l = [s for s in string]
		for S, num in enumerate(l):
			#print S, num
			num = int(num)

			if (num_people_standing + need_to_invite) >= S:
				num_people_standing += num
			else:
				need_to_invite += S - (num_people_standing + need_to_invite)
				num_people_standing += num
				#print need_to_invite

		print "Case #{0}: {1}".format(index, need_to_invite)
