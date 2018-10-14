import os

def method1(mushrooms):
	current = 0
	total = 0
	for x in mushrooms:
		if x>= current:
			current = x
			continue
		else:
			total += current-x
		current = x
	return total

def method2(mushrooms):
	rate = 0
	for i in range(1, len(mushrooms)):
		if mushrooms[i-1] - mushrooms[i] > rate:
			rate = mushrooms[i-1] - mushrooms[i] 
	deduct = 0
	total = 0
	for i in range(len(mushrooms)):
		if i == len(mushrooms)-1:
			break
		x = mushrooms[i]
		#total += min(rate, x-deduct)
		total += min(rate, x)
		#deduct = 0
		#if x-rate>0:
			#deduct += x-rate
	return total


with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as g:
        line = f.readline()
        test_count = int(line)
        for i in range(test_count):
	    print i
        #for i in range(1):
            line = f.readline()
            line = f.readline()
            mushrooms = map(int, line.split())
            g.write('Case #%s: %s %s\n'%(str(i+1), str(method1(mushrooms)), str(method2(mushrooms))))
