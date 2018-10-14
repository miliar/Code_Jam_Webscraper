def assign(r,c,cake):
	rowsAbove = []
	for row in range(r):
		countq = cake[row].count("?")
		
		if countq != 0 and countq != c:
			cur_left = 0
			toAdd = []
			for col in range(c):
				if cake[row][col] != "?":
					cur_left = cake[row][col]
					#update things to right
					for left in toAdd:
						cake[left[0]][left[1]] = cur_left
					toAdd = []
				else:
					#update things to left
					if cur_left != 0:
						cake[row][col] = cur_left
					else:
						toAdd.append((row,col))
		if countq == c:
			#check if first row, if yes copy under later
			if row == 0 or row-1 in rowsAbove:
				rowsAbove.append(row)
			#copy row above
			else:
				cake[row] = cake[row-1]

	for row in reversed(rowsAbove):
		cake[row] = cake[row+1]

	return cake

def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		r, c = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
		cake = [[0] * c for k in range(r)]
		for j in xrange(r):
			cake[j] = [str(s) for s in raw_input()]
		cake = assign(r,c,cake)
		print "Case #{}:".format(i)
		for j in xrange(r):
			print "".join(cake[j])
  		#print "Case #{}: {} {}".format(i, n + m, n * m)
  	# check out .format's specification for more formatting options

main()