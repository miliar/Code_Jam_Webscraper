from math import sqrt, floor, ceil

f = open('C-large-1.in', 'r')

N = int(f.readline())

def is_palindrome(num):
	return str(num) == str(num)[::-1]

#def next_palindrome(num):

fair = set()

for i in range(1, 10000002):
	if is_palindrome(i) and is_palindrome(i * i):
		fair.add(i)

num = 0

for i in range(N):
	one, two = f.readline().split()

	a, b = ceil(sqrt(int(one))), floor(sqrt(int(two)))

	for j in fair:
		if j >= a and j <= b:
			num += 1

	print("Case #" + str(i + 1) + ": " + str(num))

	num = 0

print(fair)