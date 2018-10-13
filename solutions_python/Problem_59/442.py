def split_topbase(dir):
	i = dir.find('/', 1)
	if i != -1:
		return dir[1:i], dir[i:]
	else:
		return dir[1:], ''

def add_dir(dirs, dir): 
	y = 0
	tb, o = split_topbase(dir)
	if not tb in dirs:
		dirs[tb] = {}
		y += 1
	if o:
		y += add_dir(dirs[tb], o)
	return y

t = int(raw_input())
for i in xrange(t):
	n, m = map(int, raw_input().split())
	y = 0
	dirs = {'/' : {}}
	for t in xrange(n):
		add_dir(dirs, raw_input())

	for t in xrange(m):
		y += add_dir(dirs, raw_input())

	print 'Case #%i: %i' % (i + 1, y)
