# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def check(number):
	converted = str(number)
	for i in xrange(0, len(converted) - 1):
		if  converted[i] > converted[i+1]:
			return False
	return True

def checkspecial(number):
	converted = str(number)
	for i in xrange(0, len(converted) - 1):
		if converted[i] != '1':
			return False
	if converted[-1] != '0':
		return False
	return True

def final(number):
	if check(number):
		return str(number)
	converted = str(number)
	for i in xrange(0, len(converted) - 1):
		if  converted[i] >= converted[i+1]:
			lis = list(converted)
			lis[i] = str(int(converted[i]) - 1)
			suffix = '9' * (len(str(number)) - 1 - i)
			if lis[0] == '0':
				return  "".join(lis[1:i+1]) + suffix
			return 	"".join(lis[:i+1]) + suffix 	
	


def output(number):
	if checkspecial(number):
		return '9' * (len(str(number)) - 1)
	if check(number):
		return str(number)
	converted = str(number)
	severed   = converted[:-1]
	prefix    = long(severed) -1
	tocheck   = str(prefix) + '9'
	return str(tocheck)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = long(raw_input())  # read a list of integers, 2 in this case

  print "Case #" + str(i) + ": " + final(n)
  # print long(str(n)[:-1])
  # if "5" < "4":
  #   print "yes"
  # check out .format's specification for more formatting options