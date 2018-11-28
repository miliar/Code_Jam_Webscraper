def get_int(s):
	return int(s[:(len(s)-1)])
	
def get_list(s):
	s = s[:len(s)-2]
	return s.split(' ')

def process_file(filename):
	fin = open(filename,'r')
	n = get_int(fin.readline())
	for i in range(0,n):
		conf1 = {}
		conf2 = {}
		r1 = get_int(fin.readline())
		for ii in range(0,4):
			conf1[ii+1] = get_list(fin.readline())
		r2 = get_int(fin.readline())
		for ii in range(0,4):
			conf2[ii+1] = get_list(fin.readline())
		t = [val for val in conf1[r1] if val in conf2[r2]]
		if len(t)==1:
			print 'Case #'+str(i+1)+':', t[0]
		elif len(t)>1:
			print 'Case #'+str(i+1)+':', 'Bad magician!'
		else:
			print 'Case #'+str(i+1)+':', 'Volunteer cheated!'
	return 0
	

if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
		ys.exit()	
	l = process_file(sys.argv[1])