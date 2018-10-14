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
6
1 10.0000 50.0000
0.2000 50.0000
2 30.0000 65.4321
0.0001 50.0000
100.0000 99.9000
2 5.0000 99.9000
30.0000 99.8999
20.0000 99.7000
2 0.0001 77.2831
0.0001 97.3911
0.0001 57.1751
2 100.0000 75.6127
70.0263 75.6127
27.0364 27.7990
4 5000.0000 75.0000
10.0000 30.0000
20.0000 50.0000
300.0000 95.0000
40.0000 2.0000
""".lstrip())

def case_reader(fileobj):
	n, v, x = map(float, fileobj.readline().strip().split())
	n = int(n)
	s = []
	for i in range(n):
		s.append(map(float,fileobj.readline().strip().split()))
	return {'n':n, 'v':v, 'x':x, 's':s}

dt = {
	'^':(-1,0),
	'>':(0,1),
	'<':(0,-1),
	'v':(1,0)
}
def case_solver(**arg):
	x = arg['x']
	v = arg['v']
	sv = [0,0,0]
	svx = [0,0,0]
	v *= 10000
	for i in arg['s']:
		#print i[1], (i[1] - x)
		i[0] *= 10000
		if abs((i[1] - x)) * 1000 < 0.0001:
			sv[0] += i[0]
		elif i[1] > x:
			sv[1] += i[0]
			svx[1] += i[0] * (i[1] - x) 
		else:
			sv[2] += i[0]
			svx[2] += i[0] * (x - i[1])
	#print sv
	#print svx
	tmax = max(svx[1], svx[2])
	if abs(tmax) < 0.00001 and sv[0] > 0:
		return str(v/sv[0])
	try:
		return str(tmax * v / (svx[2] * sv[1] + svx[1] * sv[2] + sv[0] * tmax))
	except ZeroDivisionError:
		return "IMPOSSIBLE"


	return str(arg)

if __name__ == '__main__':
	main()
	pass