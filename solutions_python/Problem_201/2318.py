from heapq import heappush, heappop
with open("input.in") as file_in, open("output.out", "w+t") as output_file:
	tests = int(file_in.readline())
	count = 1
	for i in file_in:
		list_input = i.split(' ')
		N,K = int(list_input[0]), int(list_input[1])
		
		minR, maxR = 0, 0
		if (N != K):
			thress = []
			heappush(thress, -N)
			for i in range(0, K - 1):
				current_element = -heappop(thress)
				heappush(thress, -int((current_element - 1) / 2))
				heappush(thress, -(int((current_element - 1) / 2) + 1 * (current_element % 2 == 0)))
	
			current_element = -heappop(thress)
			# print(thress)
			minR = min(int((current_element - 1) / 2), int((current_element - 1) / 2) + 1 * (current_element % 2 == 0))
			maxR = max(int((current_element - 1) / 2), int((current_element - 1) / 2) + 1 * (current_element % 2 == 0))
						
			
		output_file.write("Case #{}: {} {}\n".format(count,maxR, minR))
				
		count += 1 
		