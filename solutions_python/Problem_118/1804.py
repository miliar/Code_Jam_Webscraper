def generate():
	f = open('palindrome-squares.txt')
	table,r = [], 10**14
	while True:
		d = f.readline()
		if not d:
			break
		d = int(d)
		if d <= r:
			table.append(d)
		else :
			break
	f.close()
	return table

def main():
	out = open('C-large1-0.out','w')
	f = open('C-large1-0.in')
	table = generate()
	t = int(f.readline())

	for i in range(1,t+1):
		line = f.readline()[:-1].split(' ')
		a,b = int(line[0]), int(line[1])
		res = 0
		for j in table:
			if j >= a and j <= b:
				res += 1
		out.write('Case #%d: %d\n' % (i, res))
	out.close()
	f.close()
if __name__ == "__main__":
	main()
