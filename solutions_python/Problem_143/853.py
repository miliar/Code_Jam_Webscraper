f = open('input.txt')
r = f.readlines()
f.close()

num_cases = int(r[0].strip())

curr = 1
answers = []
while (num_cases != 0):
	a_max,b_max,k_max = r[curr].strip().split()
	curr += 1
	a_s = range(int(a_max))
	b_s = range(int(b_max))
	k_s = range(int(k_max))
	winners = 0
	for a in a_s:
		for b in b_s:
			if (a&b) in k_s:
				winners += 1
	answers.append(winners)
	num_cases -= 1
###################################

case = 1
f = open('lottery.out','w')
for answer in answers:
	f.write("Case #{0}: {1}\n".format(case,answer))
	case += 1
f.close()

# case = 1
# for answer in answers:
# 	print("Case #{0}: {1}".format(case,answer))
# 	case += 1