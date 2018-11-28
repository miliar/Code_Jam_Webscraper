def next(number):
	if number == 1:
		return 0
	elif number == 0:
		return 2
	else:
		return number+1
	
def bla(number):
	dict = {}
	resulting_number = ''
	next_small_number = 1
	for letter in number:
		if not letter in dict:
			dict[letter] = next_small_number
			next_small_number = next(next_small_number)
		resulting_number += str(dict[letter])
	print number, "can be ", resulting_number
	return resulting_number
			

def min_base(number):
	max = 0
	for letter in number:
		x = int(letter)
		if x > max:
			max = x
	print number, "should be in base",max+1
	return max+1



#f = open("A-sample.in")
f = open("/home/emre/Download/A-small-attempt0.in")
g= open("output.txt","w")
numline=int( f.readline().strip("\n"))
for i in xrange(numline):
	print "%d out of %d" %(i+1, numline)
	number = f.readline().strip("\n")
	result = bla(number)
	#print min_base(result)
	real_value = int(result, min_base(result))
	#print result, real_value
	g.write("Case #%d: %s\n" % (i+1 , real_value))
g.close()
f.close()
