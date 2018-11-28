def func(x, lst):
	k = 0
	while k in range(len(lst)-1):
		if lst[k] > x and lst[k+1] < x:
			return k
		k += 1
	return k


fr = open("in.txt", "r")
fw = open("out.txt", "w")
T = int(fr.readline())
for i in range(T):
	fw.write("Case #" + str(i+1) + ": ")
	n = int(fr.readline())
	l1 = [float(x) for x in fr.readline().split(" ")]
	lb1 = [x for x in l1]
	l2 = [float(x) for x in fr.readline().split(" ")]
	lb2 = [x for x in l2]
	l1.sort()
	l1.reverse()
	l2.sort()
	l2.reverse()
	lb1.sort()
	lb1.reverse()
	lb2.sort()
	lb2.reverse()
	count = 0
	for j in range(n):
		if l1[0] > l2[0]:
			b = l2.pop()
			a = l1.pop(func(b, l1))
			count += 1
		else:
			b = l2.pop(func(l1[0], l2))
			a = l1.pop()
	fw.write(str(count) + " ")
	count = 0
	for j in range(n):
		a = lb1.pop(0)
		if a > lb2[0]:
			b = lb2.pop()
			count += 1
		else:
			b = lb2.pop(func(a, l2))
	fw.write(str(count) + "\n")



