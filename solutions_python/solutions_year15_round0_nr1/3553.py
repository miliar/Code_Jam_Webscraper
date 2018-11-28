
iteration = int(raw_input())
solutions = []
for i in range(iteration):
	shyness = raw_input()
	additional_sum = 0
	original_sum = 0
	for j in range(int(shyness[0])+1):
		if j>(original_sum+additional_sum):
			additional_sum = j - original_sum
		original_sum = original_sum + int(shyness[j+2])
	solutions.append('Case #' + str(i+1) + ': ' + str(additional_sum))

for solution in solutions:
	print solution