





def flip(cakes, at, k):
	for i in range(at, at + k):
		if '+' == cakes[i]:
			cakes[i] = '-'
		else:
			cakes[i] = '+'

t = int(input())
for case_number in range(1, t + 1):
	cakes_s, k_s = input().split(" ")[:2]
	k = int(k_s)
	cakes = list(cakes_s)
	
	result = 0
	
	end_flip = len(cakes) - k + 1;
	for a in range(end_flip):
		if cakes[a] == '-':
			flip(cakes, a, k)
			#print("cakes", "".join(cakes), "k",k)
			result += 1
	
	for a in range(end_flip, len(cakes)):
		if cakes[a] == '-':
			result = "IMPOSSIBLE"
			break
	print("Case #{}: {}".format(case_number, result))
	

