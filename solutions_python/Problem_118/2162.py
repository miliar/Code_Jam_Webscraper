def is_square(number):
	x = number // 2
	if x == 0:
		return True
	seen = set([x])
	while x * x != number:
		x = (x + (number // x)) // 2
		if x in seen: return False
		seen.add(x)
  
	if isPalindrome(str(x)):
		return True
		
	return False

def isPalindrome(string):
    return (string == string[::-1])
    
input = 'C:\\Users\\William\\Desktop\\C-small-attempt0.in'
output = 'C:\\Users\\William\\Desktop\\C-small.out'
f = open(input, "r")
f1 = open(output, "w")
cases = f.readline()

count = 1

for x in range(int(cases)):
	line = f.readline().split()
	min = int(line[0])
	max = int(line[1]) + 1
	counter = 0
	
	for i in range(min, max):
		if is_square(i) and isPalindrome(str(i)):
			counter += 1
			
	out_line = "Case #" + str(count) + ": " + str(counter) + '/n'
	count += 1
	f1.write(out_line)