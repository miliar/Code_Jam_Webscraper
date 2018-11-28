def generate_trees(n, A, B, C, D,x,y, M):
	trees = [(x, y)]
	for i in range(1, n):
		x = (A*x + B) % M
		y = (C*y + D) % M
		trees.append((x, y))
	return trees

def find_num(trees):
	counter = 0
	for i, t1 in enumerate(trees[:-2]):
		for j, t2 in enumerate(trees[i+1:-1]):
			for t3 in trees[j+i+2:]:
				center_x = (t1[0] + t2[0] + t3[0] + 0.0)/3 - (t1[0] + t2[0] + t3[0])/3
				center_y = (t1[1] + t2[1] + t3[1] + 0.0)/3 - (t1[1] + t2[1] + t3[1])/3
				if center_x == 0 and center_y == 0:
					counter += 1
	return counter

def main():
	num_cases = input()
	for i in range(1, num_cases + 1):
		n, A, B, C, D, x, y, M = map(int, raw_input().split())
		print "Case #%d: %d" % (i, find_num(generate_trees(n, A, B, C, D, x, y, M)))



if __name__=="__main__":
	main()
