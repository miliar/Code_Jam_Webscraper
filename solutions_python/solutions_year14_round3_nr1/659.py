import re
from math import ceil
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
		if test.count <= 10:
			print f.__name__
			print "input: %s" % map(repr, args)
			print "output: %s" % str(result)
		return result
	return _f


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
				buf = f.readline()
				buf = buf.split("/")
				P, Q = supressDivision(buf[0], buf[1])
				val = float(P)/float(Q)

				buf2 = []
				buf2.append(val)
				buf2.append(P)
				buf2.append(Q)

				inputs.append(buf2)
		return n, inputs


def supressDivision(P, Q):
	pbuf = int(P)
	qbuf = int(Q)

	for prime in primes:
		while ((pbuf % prime == 0) and (qbuf % prime == 0)):
			pbuf = pbuf/prime
			qbuf = qbuf/prime

		if prime > pbuf:
			break
	return pbuf, qbuf




def getPrime(maxNum):
	result = []
	i = 2
	while i <= maxNum:
		flag = True;
		for prime in result:
			flag = flag and (i % prime != 0)
		if flag:
			result.append(i)
		i += 1
	return result

primes = getPrime(10000)
#input -> String with \n
@test
def process_aux(input):
	cnt = 0
	val = input[0]
	P = input[1]
	Q = input[2]
	while val < 1:
		val = val*2
		cnt += 1

	if cnt > 40 or not isDivisibleByTwo(Q):
		return -1
	else:
		return cnt

def isDivisibleByTwo(num):
	if(num <= 3):
		return (int(num)%2 == 0)

	div = int(num)/2
	mod = int(num)%2

	if(mod == 0):
		return isDivisibleByTwo(div)
	else: 
		return False


def writeFile(n, outputs, path = 'd:\small-practice.out'):
	with open(path, 'wb+') as f:
		for i in range(1, n+1):	#1 ~ n
			out = outputs[i-1]	#0 ~ (n-1)
			if out != -1:
					f.write("Case #%s: %d\n" % (i, out))	#Case #(1-n): (...)\n
			else:
					f.write("Case #%s: impossible\n" % (i))
				


file1 = "A-small-attempt0"

print "hi"

n, ins = readFile(file1 + ".in")
print n
#print ins
outs = process(n, ins)
print outs
writeFile(n, outs, file1 + "output.txt")
print "done!"