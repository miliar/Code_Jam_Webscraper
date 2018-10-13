T = input()

for t in range(T):
	ans1 = input()
	arr1 = list()
	for i in range(4):
		arr1.append(map(int, raw_input().split()))
	ans2 = input()
	arr2 = list()
	for i in range(4):
		arr2.append(map(int, raw_input().split()))
	


	if len(set(arr1[ans1-1] + arr2[ans2-1])) == 7:
		print "Case #%d: %d" % (t+1, list(set(arr1[ans1-1]).intersection(set(arr2[ans2-1])))[0])
	elif len(set(arr1[ans1-1] + arr2[ans2-1])) == 8:
		print "Case #%d: Volunteer cheated!" % (t+1)
	else: print "Case #%d: Bad magician!" % (t+1)