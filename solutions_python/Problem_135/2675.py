def main():
	out_file = open("out1.txt", 'w')
	T = int(raw_input())

	for i in xrange(T):
		x = int(raw_input())
		x_mat = [[], [], [], []]
		y_mat = [[], [], [], []]
		x_mat[0] = map(int, raw_input().split())
		x_mat[1] = map(int, raw_input().split())
		x_mat[2] = map(int, raw_input().split())
		x_mat[3] = map(int, raw_input().split())
		y = int(raw_input())
		y_mat[0] = map(int, raw_input().split())
		y_mat[1] = map(int, raw_input().split())
		y_mat[2] = map(int, raw_input().split())
		y_mat[3] = map(int, raw_input().split())
		print x_mat[x - 1]
		print y_mat[y - 1]
		len_to_check = len(set(x_mat[x - 1]) - set(y_mat[y - 1]))
		print len_to_check
		if len_to_check == 3:
			out_file.write("Case #%d: %d\n" % ((i+1), list(set(x_mat[x - 1]) & set(y_mat[y - 1]))[0]))
		elif len_to_check == 4:
			out_file.write("Case #%d: Volunteer cheated!\n" % (i+1))
		else:
			out_file.write("Case #%d: Bad magician!\n" % (i+1))
	out_file.close()


if __name__ == "__main__":
	main()