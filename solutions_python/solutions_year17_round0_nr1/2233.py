
def flipOrRaise(pancake, fromIndex, length):
	if fromIndex + length > len(pancake):
		raise
	for i in range(fromIndex, fromIndex + length):
		pancake[i] ^= 1
	return pancake

def flipflipflip(pancake, k):
	n_flips = 0
	for i in range(0, L):
		if pancake[i] == 1:
			continue
		try:
			pancake = flipOrRaise(pancake, i, k)
			n_flips += 1
		except:
			raise
	return n_flips
	
	
if __name__ == '__main__':
	t = int(input()) 
	for case_num in range(1, t + 1):
		[pancake_str, k_str] = input().split(" ")
		pancake = [1 if c == '+' else 0 for c in pancake_str]
		k = int(k_str)
		
		n_happy = sum(pancake)
		L = len(pancake)
		
		# everyone's happy
		if n_happy == L:
			output = 0
		# everyone can be happy easily
		elif n_happy == 0 and L % k == 0:
			output = int(L/k)
		else:
			try:
				output = flipflipflip(pancake, k)
			except:
				output = 'IMPOSSIBLE'
			
		print("Case #{}: {}".format(case_num, output))
	exit(0)