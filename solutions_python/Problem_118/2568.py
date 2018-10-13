with open(r'D:\my_stuff\Google Drive\documents\SCHOOL\Programming\Python\Google Code Jam 2013\codejam3.in', 'r') as f:
	data = f.read().split()[1:]

def nChunks(iterable, n):
	return [iterable[i:i+n] for i in range(0, len(iterable), n)]
	
data = nChunks(data, 2)
split_data = [[int(i) for i in j] for j in data]
	
def isPalindrome(n):
	nStr = str(int(n))
	return nStr == nStr[::-1]
	
def isFairSquare(n):
	root = n**0.5
	if isPalindrome(n) and float(n%root) == 0.0 and isPalindrome(root):
		return True
	else: return False


	
final = []
for i in range(len(split_data)):
	startRange = split_data[i][0]
	stopRange = split_data[i][1]
	count = 0
	n = startRange
	sqr = n**0.5
	count = 0
	while n <= stopRange:
		if float(n%sqr) == 0.0 and isPalindrome(n) and isPalindrome(sqr): count += 1
		n += 1
		sqr = n**0.5
	final.append('Case #{}: {}'.format(i+1, count))
with open(r'D:\my_stuff\Google Drive\documents\SCHOOL\Programming\Python\Google Code Jam 2013\codejam3results.txt', 'w') as f:
	for elem in final:
		f.write(elem + '\n')