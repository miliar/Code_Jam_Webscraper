import itertools
import time

start_time = time.clock()

input = open("C-small-attempt1.in")
output = open("C-small.out", 'w')

#precompute powers of 2 up to 10^6
p = 1
powers = [p]
while p < 10**6:
	p *= 2
	powers.append(p)
	
	
#convert int into binary representation as array 0s and 1s
def int_to_bin_array(num):
	bin = []
	start = 0
	while powers[start+1] <= num:
		start += 1
	r = range(start+1)
	r.reverse()
	for i in r:
		if num - powers[i] >= 0:
			num -= powers[i]
			bin.append(1)
		else:
			bin.append(0)
	return bin
	
#add binary list to int and return int	
def add_as_sean(num1, num2):
	num2decimal = 0
	for i in range(len(num2)):
		num2decimal += num2[len(num2) - i - 1] * powers[i]
	return num1 + num2decimal
	
def count_as_sean(group):
	total = 0
	for i in group:
		total = add_as_sean(total, i)
	return total

#add 2 binary lists and return binary list
def add_as_patrick(num1, num2):
	num1len = len(num1)
	num2len = len(num2)
	if num1len > num2len:
		longer = num1
		shorter = num2
		long_len = num1len
		short_len = num2len
	else:
		longer = num2
		shorter = num1
		long_len = num2len
		short_len = num1len
	
	result = range(long_len)

	for i in range(1, short_len + 1):
		result[long_len - i] = (longer[long_len - i] + shorter[short_len - i]) % 2

	for i in range(long_len - short_len):
		result[i] = longer[i]
		
	return result
		
def count_as_patrick(group):
	total = [0]
	for i in group:
		total = add_as_patrick(total, i)
		
	return add_as_sean(0,total)
	
lines = input.readlines()
num_cases = int(lines.pop(0))

for case in range(num_cases):
	
	num_candies = int(lines.pop(0))
	candies = lines.pop(0).replace('\n','').split(' ')
	for i in range(len(candies)):
		candies[i] = int(candies[i])
	
	bin_candies = map(int_to_bin_array, candies)
	
	#check combinations of candies
	best_value = -1
	
	r = range(1,len(candies))
	iexs = range(len(candies))
	for i in r:
		for comb in itertools.combinations(iexs,i):
			g1p = map(lambda x: bin_candies[x], comb)
			comb2 = [x for x in iexs if x not in comb]
			g2p = map(lambda x: bin_candies[x], comb2)

			if count_as_patrick(g1p) == count_as_patrick(g2p):
				count = count_as_sean(g1p)
				if count > best_value:
					best_value = count

	s = "Case #" + str(case+1) + ": "
	if best_value < 0:
		s += "NO"
	else:
		s += str(best_value)
	output.write(s + "\n")
	#print s
	
print "time:" + str(time.clock() - start_time)