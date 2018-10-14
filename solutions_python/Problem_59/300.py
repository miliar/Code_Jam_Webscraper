from sys import argv



def count(path, master):
	count = 0
	split = path.split('/')[1:]
	curr_p = ''
	for p in split:
		curr_p += p
		if(not curr_p in master.keys()):
			master[curr_p] = 1
			count += 1
			
	return count



if __name__ == '__main__':

	file = open(argv[1])
	tests = int(file.readline())

	for t in range(tests):
		master = {}
		to_s = file.readline().strip('\n').split()
		n, m = int(to_s[0]), int(to_s[1])
		for i in range(n):
			path = file.readline().strip('\n').split('/')[1:]
			curr_p = ''
			for p in path:
				curr_p += p
				master[curr_p] = 1
		tot = 0
		for j in range(m):
			path = file.readline().strip('\n')
			tot += count(path, master)
		
		print("Case #%i: %i"%(t+1, tot))
