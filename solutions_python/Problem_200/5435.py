def send_toanother(number, index, g):
	shadow_number = number
	n = str(shadow_number)
	size = len(n)-1
	j = size
	if j != 0:
		while j > 0:
			if n[j] < n[j-1]:
				shadow_number -= 1
				n = str(shadow_number)
			else:
				j -= 1
	print("Case #%d: %d" % (index+1, shadow_number))
	g.write("Case #%d: %d\n" % (index+1, shadow_number))

def do_something():
	f = open('B-small-attempt0.in', 'r')
	g = open('B-small-attempt0.txt', 'w')
	start = 1
	arr = []
	for line in f:
		if start == 1:
			start = 0
			continue
		arr.append(int(line))
	for index in range(0,len(arr)): #len(arr)
		send_toanother(arr[index], index, g)



do_something()