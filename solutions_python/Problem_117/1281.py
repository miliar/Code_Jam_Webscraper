def main():
	with open("B-large.in", "r") as f:
		num_test_cases = int(f.readline())
		
		for test_case_index in range(num_test_cases):
			lawn = []
			N, M = f.readline().split(" ")
			N = int(N)
			M = int(M)
			for i in range(N):
				tokenized_line = f.readline().split(" ")
				row = [int(token) for token in tokenized_line]
				lawn.append(row)
			
			if is_possible_to_get_pattern(lawn, N, M):
				print  "Case #" + str(test_case_index + 1) + ": YES"
			else:
				print  "Case #" + str(test_case_index + 1) + ": NO"


def is_possible_to_get_pattern(lawn, N, M):
	height_to_coors_map = {}
	heights = []
	for i in range(N):
		for j in range(M):
			if lawn[i][j] not in height_to_coors_map:
				heights.append(lawn[i][j])
				height_to_coors_map[lawn[i][j]] = [(i,j)]
			else:
				height_to_coors_map[lawn[i][j]].append((i,j))

	heights.sort()
	heights.reverse()
	
	remaining_rows_columns = set()
	for i in range(N):
		remaining_rows_columns.add((0,i))

	for i in range(M):
		remaining_rows_columns.add((1,i))

	current_lawn = [[heights[0]]*M for i in range(N)]
	for i in range(1, len(heights)):
		coors_not_to_mow = height_to_coors_map[heights[i-1]]
		for coor in coors_not_to_mow:
			remaining_rows_columns.discard((0, coor[0]))
			remaining_rows_columns.discard((1, coor[1]))

		for row_column in remaining_rows_columns:
			# If row
			if row_column[0] == 0:
				for j in range(M):
					current_lawn[row_column[1]][j] = heights[i]
			# If column
			else:
				for j in range(N):
					current_lawn[j][row_column[1]] = heights[i]

	is_possible = True
	for i in range(N):
		for j in range(M):
			if lawn[i][j] != current_lawn[i][j]:
				is_possible = False
				break
		if not is_possible:
			break

	return is_possible

if __name__ == "__main__":
	main()
