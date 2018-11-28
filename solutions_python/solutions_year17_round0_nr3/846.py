
def add(num, freq, hm):
	if num not in hm:
		hm[num] = 0
	hm[num] += freq

def get(x, k):
	
	if x % 2:
		y = x-1
	else:
		y = x+1
	freq = {x: 1, y:0}
	numbers = sorted([x, y])[::-1]

	while numbers[-1] != -1:
		
		for num in numbers[-2:]:
				
			add(num//2, freq[num], freq)
			add(num//2-(1-num%2), freq[num], freq)

		numbers = sorted(list(freq.keys()))[::-1]

	# print(numbers)

	aggr_freq = 0
	for num in sorted(freq.keys())[::-1]:
		aggr_freq += freq[num]
		# print(num, freq[num], aggr_freq)
		if aggr_freq >= k:
			if num == 0:
				return (0, 0)
			return(num//2, (num-1)//2)

			
case_count = int(input())
for case in range(case_count):
	
	n, k = [int(x) for x in input().split()]
	
	print("Case #{0}: {1} {2}".format(case+1, *get(n, k)))
