import string

f = open('A-small-attempt0.in', 'r')
n = int(f.readline())
for count in range(n):
	line1 = int(f.readline())
	nums1 = []
	for i in range(4):
		num_str = f.readline()
		nums1.append([int(s) for s in string.split(num_str, ' ')])

	line2 = int(f.readline())
	nums2 = []
	for i in range(4):
		num_str = f.readline()
		nums2.append([int(s) for s in string.split(num_str, ' ')])

	x = 0
	ans = 0
	for num in nums1[line1-1]:
		if num in nums2[line2-1]: 
			x += 1
			ans = num

	output = 'Case #'+str(count+1)+': '
	if x == 0:
		print output+'Volunteer cheated!'
	elif x == 1:
		print output+str(ans)
	else:
		print output+'Bad magician!'