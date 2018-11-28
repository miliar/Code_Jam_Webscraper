import sys
print sys.argv

test_case = 0
test_case_count=0
f=open(sys.argv[1])
test_case = int(f.readline())


while test_case_count < test_case:
	test_case_count += 1
	friends = 0
	standing = 0
	l = f.readline()
	args = l.split(' ')
	level = int(args[0])
	disp = args[1]
	
	for i in range(0,level+1):
		if standing < i:
			friends += i - standing
			standing += i - standing
		standing+= int(disp[i])

	with open('output','a') as out:
		out.write('Case #'+ str(test_case_count)+': ')
		out.write(str(friends))
		out.write('\n')