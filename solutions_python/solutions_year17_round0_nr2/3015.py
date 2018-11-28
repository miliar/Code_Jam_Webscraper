from math import log10,floor
def get_last_tidy_number(arr):
	for n in range(len(arr)):
		for i in range(len(arr)):
			if i+1 < len(arr) and arr[i] > arr[i+1]:
				arr[i] -= 1
				for j in range(i+1, len(arr)):
					arr[j] = 9
	return int(''.join(str(char) for char in arr))

n = int(input())
for i in range(n):
	print('Case #'+str(i+1)+': ' + str(get_last_tidy_number([int(char) for char in input()])))
