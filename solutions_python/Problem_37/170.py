from __future__ import with_statement

def base(num, n):
    b = n
    a = 1
    p = 0
    ans = [0]
    while a < num:
	a *= n
	p += 1
    if a != num:
	a /= n
	p -= 1
    while (a <= num) and num:
	ans[-1] += 1
	num -= a
	if num == 0:
	    break
	if num < 0:
	    foaisd
	while a > num:
	    a /= n
	    p -= 1
	    ans.append(0)
    return ans

h = {}
def f(n, b, prev = None):
    if prev == None:
	prev = []
    if n < 1000:
	prev.append(n)	
	if (n,b) in h:
	    for i in prev:
	        h[(i,b)] = h[(n, b)]
	    return h[(n,b)]
    
	h[(n,b)] = False
    l = base(n, b)
    if l == [1]:
	for i in prev:
	    h[(i,b)] = True
    return f(sum(map(lambda x: x*x, l)), b, prev)
    

def process_case(data, out):
    a = data.readline().strip("\n").split(" ")
    print a
    bases = map(int, a)
    fit = False
    if 2 in bases:
	bases = bases[1:]
    i = 2
    while not fit:
	for b in bases:
		if f(i, b):
		    fit = True
		    continue
		fit = False
		i += 1
		break
    return "%d" % i

def process_file(fname):    
    
    with open(fname, "r") as data:
	with open("answer_" + fname, "w") as answer:
	    n = int(data.readline().strip("\n"))
	    for i in range(n):
		answer.write("Case #%d:" % (i+1))
		a = process_case(data, answer)
		answer.write(" %s" % a)
		answer.write("\n")
#process_file("asample.txt")
process_file("A-small-attempt1.in")
#processFile("1AA-large.in")