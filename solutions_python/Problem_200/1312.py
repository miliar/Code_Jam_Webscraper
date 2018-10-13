import sys
import math


n = int(input())
for i in range(n):
	number = str(input())
	for j in reversed(range(1, len(number))):
		if (number[j] < number[j-1]):
			number = number[:j-1] + str(int(number[j-1])- 1) + "9" * (len(number)-j)
	print("Case #" + str(i+1) + ": " + str(int(number)))