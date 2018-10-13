import math
def rev_num_sort(num):
	strs = str(num)
	return all(int(x) <= int(y) for x, y in zip(strs, strs[1:]))

def num_digits(num):
	return len(str(num))

def num_first_digit(num):
	return int(str(num)[0])

def isPower (num, base):
	logNum = math.log(num, base)
	power = int(logNum + 0.5)
	return base ** power == num

def printCase(i, num):
	print 'Case #'+str(i)+':',num	

with open('B-small-attempt5.in') as f:
	inputs = [int(x) for x in f]
	i = 0
	for num in inputs[1:]:
		i += 1
		if rev_num_sort(num):
			printCase(i, num)
		elif isPower(num, 10):
			printCase(i, num - 1)
		else:
			# numDig = num_digits(num - 1) - 1
			# ten = 10**numDig
			# firstDig = num_first_digit(num - 1)
			# startDig = ten*firstDig
			loopCtr = num
			# print startDig
			while loopCtr > 10:
				if (rev_num_sort(loopCtr)):
					printCase(i, loopCtr)
					break
				else:
					loopCtr -= 1