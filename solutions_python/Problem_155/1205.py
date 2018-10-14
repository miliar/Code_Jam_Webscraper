import sys
if __name__ == "__main__":
	filename = sys.argv[1]
	with open(filename,"r") as f:
		data = f.readlines()
	data = [i.replace("\n","") for i in data]
#	num_of_test_cases = int(raw_input(""))
	num_of_test_cases = int(data[0])
	test_cases_results = []
#	import pdb;pdb.set_trace()
	for i in range(num_of_test_cases):
#		s_max,audience_desc = raw_input("").split(" ")
		s_max,audience_desc = data[i+1].split(" ")
		s_max = int(s_max)
		num_to_invite = 0
		num_standing_up = 0
		for shyness_level,num_of_people in enumerate(audience_desc):
			if num_standing_up >= shyness_level:
				num_standing_up += int(num_of_people)
			else:
				num_to_invite += shyness_level - num_standing_up
				num_standing_up+= int(num_of_people) + (shyness_level - num_standing_up)
		test_cases_results.append(num_to_invite)
	for i,res in enumerate(test_cases_results):
		print "Case #%d: %d" % (i+1,res)
