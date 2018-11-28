import sys
f = open(sys.argv[1],'r')
case = int(f.readline())
for pointer in range(0,case):
	first_s = int(f.readline())
	int_arr = []
	for s_pointer in range(0,4):
		int_arr.append(f.readline().split())
	second_s = int(f.readline())
	sec_arr = []
	for s_pointer in range(0,4):
		sec_arr.append(f.readline().split())
	first = int_arr[first_s-1]
	second = sec_arr[second_s-1]
	ans = [val for val in first if val in second]
	if(len(ans) == 1):
		print 'Case #'+str(pointer+1)+': '+str(ans[0])
	elif(len(ans) == 0):
		print 'Case #'+str(pointer+1)+': Volunteer cheated!'
	else:
		print 'Case #'+str(pointer+1)+': Bad magician!'
