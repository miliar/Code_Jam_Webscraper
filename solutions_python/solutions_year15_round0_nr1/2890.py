import sys
sys.stdout = open("c:\\out.txt", "w")
f = open('A-large.in', 'r')
test_cases = int(f.readline())

i = 0
for line in f:
	tmp = line.split()
	smax = int(tmp[0])
	audience = [int(n) for n in list(tmp[1])]
	added_people = 0
	tmp_sum = 0
	
	for n in range(smax+1):
		if 0 not in audience:
			break
		tmp_sum = sum(audience[:n])
		if (tmp_sum > smax):
			break
		if (tmp_sum < n):
			sum_diff = n - tmp_sum
			audience[n] += sum_diff
			added_people += sum_diff

	print("Case #", i+1, ": ", added_people, sep='')
	i += 1
