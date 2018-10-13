import re

testcase = int(raw_input())

for i in range(1, testcase + 1, 1):
	inp = raw_input()
	event = map(int, re.findall(r'\d+', inp))

	no_of_event = event.pop(0)

	event = list(set(event))
	event.sort()

	first = event.pop(0)
	event.insert(0, first)

	sub = []

	for x in event:
		for z in event:
			if x == z:
				continue

			sub.append(abs(z - x))

	event = list(set(sub))

	if len(event) == 1:
		T = event.pop(0)
	else:
		while 1:
			event.sort()
			head = event.pop(0)

			if head == 0: 
				break
			else:
				T = head

			mod = [head]

			for x in event:
				p = x % head
				mod.append(p)

			event.append(head)
			event = list(set(mod))

	if first % T == 0:
		y = 0
	else:
		y = T - (first % T)

	print "Case #%d: %d" % (i, y)

