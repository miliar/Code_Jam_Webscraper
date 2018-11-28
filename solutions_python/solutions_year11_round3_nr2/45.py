def dist_at(a,c,dist):
	return dist[a%c]
	
def normal_time(n,c,dist):
	time = 0
	for star in xrange(0,n):
		length = dist_at(star,c,dist)
		time += length*2
	return time

def solve():
	test = int(raw_input())
	for case in xrange(1,test+1):
		dist = []
		input = map(int,raw_input().split())
		for i in xrange(0,len(input)):
			if i == 0:
				l = input[i]
			elif i == 1:
				t = input[i]
			elif i == 2:
				n = input[i]
			elif i == 3:
				c = input[i]
			else:
				dist.append(input[i])
		
		current = 0
	        dist_from_current = 0.0
        	for star in xrange(0,n):        
                	next = dist_at(star,c,dist)
                	time = next*2
                	if time < t:
                        	t = t - time
                        	current = star+1
                	elif time == t:
                        	current = star+1
                        	dist_from_current = 0.0
                	else:
                        	current = star
                        	dist_from_current = 0.5*t
				break

#		print current,dist_from_current
		a = current
		b = current + 1
		dist_left_to_b = dist_at(a,c,dist) - dist_from_current
		list = []
		for star in xrange(b,n):
			list.append(dist_at(star,c,dist))
		list.append(dist_left_to_b)
		count = 0
		normal = normal_time(n,c,dist)
		saved = 0
		if l != 0:
			for val in sorted(list,reverse=True):
				saved += val
				count += 1
				if count == l:
					break
		if l == 0:
			print "Case #" + str(case) + ": " + str(int(normal))
		else:
			print "Case #" + str(case) + ": " + str(int(normal-saved))

	
solve()
