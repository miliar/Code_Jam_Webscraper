
def main(path, out):
	with open(path, 'r+') as f:
		line = f.readline().replace('\n', '')
		cases_count = int(line)
		cases = []
		for i in range(0, cases_count):
			line = f.readline().replace('\n', '')
			smax = int(line.split(' ')[0])
			slvl = [int(j) for j in list(line.split(' ')[1])]
			#levels.append([smax, slvl])
			cases.append(test_case(smax, slvl, i + 1))
	with open(out, 'w+') as o:
		for l in cases:
			o.write(l + '\n')

def test(k, people, standing):
	if k == 0 and people > 0: # very first case
		return people
	if standing >= k: # if enough is stood up
		return people
	return 0

def test_case(smax, slvl, case):
	friends = 0
	standing = 0
	for k in range(0, smax + 1):
		if slvl[k] == 0:
			continue
		f = 0
		ans = test(k, slvl[k], standing)
		while(ans == 0):
			f += 1
			ans = test(k, slvl[k], standing + f)
		standing += (ans + f)
		friends += f
		f = 0
	return "Case #{0}: {1}".format(case, friends)
	print "Case #{0}: {1}".format(case, friends)

if __name__ == '__main__':
	main("C:\Users\Anders\Desktop\A-large.in", "C:\Users\Anders\Desktop\out.txt")