import sys
import math
import StringIO
import os
import re

target_dir = 'C:\\Users\\lijia_000\\Downloads'
def search_file():
	problem_id = os.path.basename(sys.argv[0]).split('.')[0].lower()
	large_list = filter(lambda x: re.match('^%s.*large.*\.in$' % problem_id, x.lower()) is not None, os.listdir(target_dir))
	if large_list:
		return max(large_list)
	small_list = filter(lambda x: re.match('^%s.*small.*\.in$' % problem_id, x.lower()) is not None, os.listdir(target_dir))
	if small_list:
		return max(small_list)
	sys.stderr.write("No file available\n")

def problem_solver(fileobj_in, fileobj_out):
	n = int(fileobj_in.readline())
	for i in xrange(n):
		result = case_solver(**case_reader(fileobj_in))
		assert(type(result) is str)
		if not result.endswith('\n'): result += '\n'
		fileobj_out.write("Case #%d: %s" % (i+1, result))
def main():
	problem_solver(f_in, f_out)

file_name = None
file_name = search_file()
if file_name:
	f_in = open(os.path.join(target_dir, file_name), 'r')
	f_out = open(os.path.basename(file_name[:-3]) + '.out', 'w')
else:
	f_out = sys.stdout
	f_in = StringIO.StringIO("""
5
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.
2 2
<^
v>
""".lstrip())

def case_reader(fileobj):
	r,c = map(int, fileobj.readline().strip().split())
	b = []
	for i in range(r):
		b.append(list(fileobj.readline().strip()))
	return {'r':r, 'c':c, 'b':b}

dt = {
	'^':(-1,0),
	'>':(0,1),
	'<':(0,-1),
	'v':(1,0)
}
def case_solver(**arg):
	r, c, b = arg['r'], arg['c'], arg['b']
	cnt = 0
	for i in range(r):
		for j in range(c):
			if b[i][j] == '.':
				continue
			found = False
			for k in range(r):
				if k != i and b[k][j] != '.':
					found = True
					break
			for k in range(c):
				if k != j and b[i][k] != '.':
					found = True
					break
			if not found:
				return "IMPOSSIBLE"
			dx,dy = dt[b[i][j]]
			ex,ey = i,j
			keep = False
			while True:
				ex += dx
				ey += dy
				if ex <0 or ex>=r or ey < 0 or ey >=c:
					break
				if b[ex][ey] != '.':
					keep = True
					break
			if not keep:
				cnt += 1
	return str(cnt)
	return str(arg)

if __name__ == '__main__':
	main()
	pass