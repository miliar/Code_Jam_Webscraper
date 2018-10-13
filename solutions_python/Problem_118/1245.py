import operator, math

def lrange(num1, num2 = None, step = 1):
	op = operator.__lt__
	
	if num2 is None:
		num1, num2 = 0, num1
	if num2 < num1:
		if step > 0:
			num1 = num2
		op = operator.__gt__
	elif step < 0:
		num1 = num2
	
	while op(num1, num2):
		yield num1
		num1 += step

palindrome = lambda s: s == s[::-1]
calculated = []
last_calculated = 0
last_square_calculated = 0

def generate_calculated(end):
	global last_calculated
	global last_square_calculated
	
	begin = last_calculated+1
	end_2 = int(math.sqrt(end)) + 1;
	for i in lrange(begin, end_2):
		square = i*i
		
		if palindrome(str(i)) and palindrome(str(square)):
			calculated.append(square)
			last_square_calculated = square
	last_calculated = end_2

with open('input.txt', 'r') as f:
	nb_tests = int(f.readline()) + 1
	for id in xrange(1, nb_tests):
		numbers = f.readline().split()
		begin = int(numbers[0]) - 1
		end = int(numbers[1]) + 1
		
		if end > last_square_calculated:
			generate_calculated(end)
		
		sublist = [i for i in calculated if i > begin and i < end]
		print "Case #%d: %d" % (id, len(sublist))
