import codecs
import sys
write = sys.stdout.write

with codecs.open("A-large.in", "r", "utf- 8") as f:
	temp = f.readlines()
	num = int(temp[0].strip())
	line = 1
	for i in xrange(num):
		t = temp[line].strip().split()
		h = int(t[0])
		w = int(t[1])
		line += 1
		array = []
		print "Case #{0}:".format(i + 1)
		for j in xrange(h):
			array.append(temp[line])
			line += 1
		possible = True
		for j in xrange(h):
			sum = 0
			for k in xrange(w):
				if array[j][k] == u"#":
					sum += 1
				elif sum % 2 != 0:
#					print "error", j, k, sum
					possible = False
					break
			if sum % 2 != 0:
				possible = False
		for k in xrange(w):
			sum = 0
			for j in xrange(h):
				if array[j][k] == u"#":
					sum += 1
				elif sum % 2 != 0:
#					print "error", j, k, sum
					possible = False
					break
			if sum % 2 != 0:
				possible = False
		if not possible:
			print u"Impossible"
		else:
			result = []
			for j in xrange(h):
				result.append([-1] * w)
			for j in xrange(h):
				for k in xrange(w):
					if array[j][k] == u"#" and result[j][k] == -1:
						result[j][k] = 0
						result[j][k + 1] = 1
						result[j + 1][k] = 1
						result[j + 1][k + 1] = 0
			for j in xrange(h):
				st = ""
				for k in xrange(w):
					if result[j][k] == -1:
						st += u"."
					if result[j][k] == 0:
						st += u"/"
					if result[j][k] == 1:
						st += u"\\"
				print st
