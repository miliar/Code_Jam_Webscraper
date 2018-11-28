import sys

tc = int(sys.stdin.readline())

for t in range(1,tc+1):
	result_str = "Case #" + str(t) + ": "
	#logic here
	ans1 = int(sys.stdin.readline().strip())
	arr1  = []
	for _ in range(4):
		line = sys.stdin.readline().strip().split()
		line = map(int,line)
		arr1.append(line)
	selected_roow_1 = arr1[ans1-1]

	ans2 = int(sys.stdin.readline().strip())
	arr2 = []
	for _ in range(4):
		line = sys.stdin.readline().strip().split()
		line = map(int,line)
		arr2.append(line)
	selected_roow_2 = arr2[ans2-1]

	common = []
	for each_one in selected_roow_1:
		for each_two in selected_roow_2:
			if(each_one == each_two):
				common.append(each_one)
	if(len(common)==1):
		result_str += str(common[0])
	elif(len(common)==0):
		result_str += "Volunteer cheated!"
	elif(len(common)>1):
		result_str += "Bad magician!"
	print result_str