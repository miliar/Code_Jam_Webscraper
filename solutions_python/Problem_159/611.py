#input_lines = open("tmp.in").read().splitlines()
#input_lines = open("A-small-attempt1.in").read().splitlines()
input_lines = open("A-large.in").read().splitlines()
#input_lines = open("B-small-attempt0.in").read().splitlines()
#input_lines = open("B-large-attempt0.in").read().splitlines()
#input_lines = open("C-small-attempt0.in").read().splitlines()
#input_lines = open("C-large-attempt0.in").read().splitlines()
#input_lines = open("D-small-attempt0.in").read().splitlines()
#input_lines = open("D-large-attempt0.in").read().splitlines()

test_num = int(input_lines[0])

for i in range(test_num):
	n = int(input_lines[2*i+1])
	mushroom = map(int, input_lines[2*i+2].split())
	first = 0
	second = 0
	prev_m = mushroom[0]
	for j in mushroom[1:]:
		if prev_m > j:
			first += prev_m - j 
		prev_m = j 
	rate = 0
	for j in range(1,len(mushroom)):
		rate = max(rate,mushroom[j-1]-mushroom[j])
	if rate > 0:
		for j in mushroom[:-1]:
			second += min(j,rate)
	print "Case #" + str(i+1) + ":",str(first),str(second)
