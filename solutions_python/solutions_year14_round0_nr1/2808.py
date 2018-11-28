import re
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if len(args) == 0:
            return x
        else:
            return f(x, n_ary_f(args[0], *args[1:]))
        # your code here
    return n_ary_f

def trace(f):
	indent = '    '
	trace.level = -1
	def _f(*args):
		trace.level += 1
		txt = '===>%s(%s)' % (f.__name__, map(repr, args))
		print indent*trace.level + txt
		try:
			result = f(*args)
			txt2 = '<===%s(%s) : %s' % (f.__name__, map(repr, args), str(result))
			print indent*trace.level + txt2
		finally:
			trace.level -= 1
		return result
	return _f

def test(f):
	test.count = 0
	def _f(*args):
		test.count += 1
		result = f(*args)
		if test.count <= 2:
			print "input: %s" % map(repr, args)
			print "output: %s" % str(result)
		return result
	return _f

def writeFile(n, outputs, path = 'd:\small-practice.out'):
	with open(path, 'wb+') as f:
		for i in range(1,n+1):
			f.write("Case #%d: %s\n" % (i, outputs[i-1]))

def process(n, inputs):
	outputs = []
	for i in range(n):
		outputs.append(process_aux(inputs[i]))
	return outputs

def readFile(path = 'd:\small-practice.in'):
		with open(path, 'rb+') as f:
			l1 = f.readline()
			n = int(l1)
			inputs = []
			for i in range(n):
				buf = []
				for j in range(2):
					rowNum = int(f.readline())
					for k in range(4):
						buf2 = f.readline()[:-1]
						if k+1 == rowNum:
							buf2 = buf2.split(" ")
							buf.append(set(int(elem) for elem in buf2))
				inputs.append(buf)
		return n, inputs

#input -> String without \n
@test
def process_aux(input):
	output =""
	intersection = input[0] & input[1]
	length = len(intersection)
	if length == 0:
		output = "Volunteer cheated!"
	elif length == 1:
		output = str(intersection.pop())
	else:
		output = "Bad magician!"
	return output



file1 = "A-small-attempt0"
file2 = "A-large-attempt0"


n, ins = readFile(file1 + ".in")
print n
#print ins
outs = process(n, ins)
#print outs
writeFile(n, outs, file1 + ".txt")
print "done!"



