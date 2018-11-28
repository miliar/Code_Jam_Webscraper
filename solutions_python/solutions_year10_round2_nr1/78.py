def get_res(test_case_lines_exist,test_case_lines_make):
	dirs_to_make = []
	dirs_exist = []
	for line in test_case_lines_make:
		dirs = list(line.split("/"))
		dirs.remove('')
		for i in range(1, len(dirs)+1):
			dir_to_add = ""
			for j in range(0, i):
				dir_to_add += dirs[j]+"."
			dirs_to_make.append(dir_to_add)
	for line in test_case_lines_exist:
		dirs = line.split("/")
		dirs.remove('')
		for i in range(1, len(dirs)+1):
			dir_to_add = ""
			for j in range(0, i):
				dir_to_add += dirs[j]+"."
			dirs_exist.append(dir_to_add)
	
	dirs_to_make = list(set(dirs_to_make))
	dirs_exist = list(set(dirs_exist))

	for dir in dirs_exist:
		if dirs_to_make.__contains__(dir):
			dirs_to_make.remove(dir)
	
	return len(dirs_to_make)
	
				
	
if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		(num_exists,num_make) = map(int,f.readline().strip().split(" "))
		test_case_lines_exist = []
		test_case_lines_make = []
		for j in xrange(num_exists):
			test_case_lines_exist.append(f.readline().strip())
		for j in xrange(num_make):
			test_case_lines_make.append(f.readline().strip())
		print "Case #%d: %s" %(i,get_res(test_case_lines_exist, test_case_lines_make))
		