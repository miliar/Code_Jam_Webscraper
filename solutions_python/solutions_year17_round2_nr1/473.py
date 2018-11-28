from timeit import default_timer as timer

def cruise_speed(d, start_pos, max_speed):
	times = [0]*len(start_pos)
	for i in xrange(len(start_pos)):
		times[i] = (d - start_pos[i]) * 1.0 / max_speed[i]
	max_time = max(times)
	return d / max_time

	
start = timer()
filename = 'A-large'
f = open(filename + '.in', 'r')
g = open(filename + '.out', 'w')
t = int(f.readline())

for i in xrange(1, t+1):
	d, n = [int(x) for x in f.readline().split(' ')]
	start_pos = [0]*n
	max_speed = [0]*n
	for j in xrange(n):
		start_pos[j], max_speed[j] = [int(x) for x in f.readline().split(' ')]
	g.write('Case #' + str(i) + ': ' + ('%.6f' % cruise_speed(d, start_pos, max_speed)) + '\n')

f.close()
g.close()
end = timer()
print (end - start)
