testcase_count = int(input())
for testcase_index in range(testcase_count):
	color_names = "ROYGBV"
	colors = list(map(int, input().split()))
	n = colors.pop(0)
	#print(colors)
	result = ""
	index = 0 if colors[0] > 0 else 2 if colors[2] > 0 else 4
	for i in range(n):
		if colors[index] == 0:
			break
		result += color_names[index]
		colors[index] = colors[index] - 1
		#print(result)
		
		# find next color
		opposite_color = (index + 3) % 6
		if colors[opposite_color] > 0:
			index = opposite_color
		else:
			smaller_neighbour = 0 if index != 0 else 2
			larger_neighbour = 4 if index != 4 else 2
			#print("%d %d" % (colors[smaller_neighbour], colors[larger_neighbour]))
			index = smaller_neighbour if colors[smaller_neighbour] >= colors[larger_neighbour] else larger_neighbour
	first_index = color_names.index(result[0])
	last_index = color_names.index(result[len(result) - 1])
	done = sum(colors) == 0 and abs(first_index % 6 - last_index % 6) > 1
	
	print("Case #%d: %s" % (testcase_index + 1, result if done else "IMPOSSIBLE"))
