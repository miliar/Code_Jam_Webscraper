
def solve(sNum):
	pos = 0
	s = list(sNum)
	if len(s) == 1:
		return ''.join(s)
	last_index = 0
	unordered = False
	for i in range(len(s)-1):
		if int(s[i]) > int(s[i+1]):
			s[i] = str(int(s[i])-1)
			unordered = True
			last_index = i
			break
	if unordered:
		for x in range(last_index+1,len(s)):
			s[x] = '9'
		return solve(s)
			
	return ''.join(s)
	

def main():
	file = open('B-large.in', 'r')
	write = open('output.txt', 'w')
	cases = int(file.readline())
	for case in range(1,cases+1):
		line = file.readline().split()
		ans = str(int(solve(line[0])))
		write.write("Case #" + str(case) + ": " + ans + "\n")
	
	file.close()
	write.close()

main()
		
			
		