import os

def find_position(s,c):
	positions = []
	count = 0
	for char in s:
		if c == char:
			positions.append(count)
		count += 1
	return positions
assert([0] == find_position('dmitri','d'))

f = open('test.txt','r')
trials = int(f.readline())
for i in xrange(1,trials+1):
	#print "TRIAL %d" % i
	answer = []
	line = f.readline().split()
	#print line
	num_composite = int(line[0])
	composite_map = {}
	for y in xrange(1,num_composite+1):
		key = ''.join(sorted(line[y][0:2]))
		val = line[y][-1]
		composite_map[key] = val
	#print "Composites are {0}".format(composite_map)
	num_antis = int(line[num_composite+1])
	anti_map = {}
	for j in xrange(num_composite+2, num_composite + 2+ num_antis):
		first = line[j][0]
		second = line[j][-1]
		if(anti_map.has_key(first)):
			anti_map[first].append(second)
		else:
			anti_map[first] = [second]
		if anti_map.has_key(second):
			anti_map[second].append(first)
		else:
			anti_map[second] = [first]
	#print "number of antis = %d" % num_antis
	#print repr(anti_map)
	recipe_length = line[-2]
	recipe = line[-1]
	#print "The recipe is: %s" % recipe
	stack = []
	counter = 0
	for s in recipe:	
		stack.append(s)
		#print "current step {0}".format(repr(stack))
		if len(stack) > 1:
			last = stack.pop()
			second_last = stack.pop()
			recent = ''.join(sorted(last+second_last))
			#print recent
			if composite_map.has_key(recent):
				stack.append(composite_map[recent])
			else:
				stack.append(second_last)
				stack.append(last)
			last_char = stack[-1]
			if anti_map.has_key(last_char):
				search_fors = anti_map[last_char]
				#print search_fors
				indexes = []
				for search_for in search_fors:
					indexe = find_position(stack,search_for)
					for thinger in indexe:
						indexes.append(thinger)
				indexes.sort()
				if(len(indexes) > 0):
					#print indexes
					stack = []
					#print "After anti "+repr(stack)
	print "Case #{0}: {1}".format(str(i),repr(stack))