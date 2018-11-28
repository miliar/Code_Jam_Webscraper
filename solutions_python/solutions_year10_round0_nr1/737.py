d = [1]
for i in xrange(1, 31):
	d.append(d[i-1] * 2 + 1)
	
def process(n, snaps):
	if d[n-1] > snaps:
		return False
	elif d[n-1] == snaps:
		return True
	else:
		return (snaps % (d[n-1] + 1)) == d[n-1]
	
	'''
	snappers = [False] * n

	for snap in xrange(snaps):
		for i in xrange(n):
		 	if not snappers[i]:
				snappers[i] = True
				break
			snappers[i] = False
	
	on = all(snappers)
	
	if snaps > d[n-1]:
		print "n=%s, snaps=%s (%s) => %s" % (n, snaps, d[n-1], on)
	
	return on
	'''
		

def main():
	file_in = open("in.txt", "r")
	file_out = open("out.txt", "w")

	for i in xrange(int(file_in.readline())):
		line = file_in.readline()
		n, snaps = [int(s) for s in line.split()]
		file_out.write("Case #%s: %s\n" % (i + 1, ['OFF', 'ON'][process(n, snaps)]))
		
	file_in.close()
	file_out.close()
	
if __name__ == "__main__":
	main()