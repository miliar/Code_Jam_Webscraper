def process(p):
	needed = 0
	people = 0
	lvl = 0
	for x in p:
		peeps = int(x)
		if lvl > people:
			a = lvl - people
			needed += a
			people += a
		lvl += 1
		people += peeps
	return needed

with open("A-large.in") as f:
	l = f.readlines()
cases = l.pop(0)
l = [x.strip().split() for x in l]
print('Cases:', cases)

count = 1
f = open('ovation_out.txt', 'w')
for x in l:
	ans = process(x[1])
	s = 'Case #' + str(count) + ': ' + str(ans)
	print(s)
	f.write(s + '\n')
	count += 1
f.close()