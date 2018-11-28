inp = open('/Users/aspittel/Downloads/B-small-attempt0 (1).in')
inp = inp.read()
inp = inp.split('\n')
write_file = open('code_jam_2.txt', 'w+')

print(inp)
# input = '''4
# 132
# 1000
# 7
# 111111111111111110'''

inp.pop(0)
inp.pop()

def find_smallest_sorted(n):
	if n < 10:
		return n
	parsed_n = list(str(n))
	if parsed_n == sorted(parsed_n): 
		return n
	starting_check = 0
	found = False
	while not found:
		if parsed_n[starting_check] < parsed_n[starting_check + 1]:
			starting_check += 1
		else:
			found = True
	for i in range(starting_check + 1, len(parsed_n)):
		parsed_n[i] = '0'
	return int(''.join(parsed_n)) - 1

		
for idx, n in enumerate(inp):
	write_file.write("Case #{}: {}\n".format(idx + 1, find_smallest_sorted(int(n))))
	
