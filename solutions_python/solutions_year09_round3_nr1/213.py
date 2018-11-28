from __future__ import with_statement
#import psyco
#psyco.full()
 
def base(n, b):
    n = str(n)[::-1]
    i = 0
    ans = 0
    for i, x in enumerate(n):
	ans += int(x) * (b ** i)
    return ans

def process_case(data, out):
    l = data.readline().strip("\n")
    print l
    s = set(l)
    ns = {l[0]:1}
    numbers = range(40)
    del numbers[1]
    ans = []
    for c in l:
	if c in ns:
	    ans.append(str(ns[c]))
	else:
	    ns[c] = numbers.pop(0)
	    ans.append(str(ns[c]))
    ans = ''.join(ans)
    b = len(s)
    if b == 1:
	b = 2
    ans = base(ans, b)

    out.write("%d\n" % ans)

def process_file(fname):    
    
    with open(fname, "r") as data:
	with open("answer_" + fname, "w") as answer:
	    n = int(data.readline().strip("\n"))
	    for i in range(n):
		answer.write("Case #%d: " % (i+1))
		a = process_case(data, answer)
		#answer.write("\n")
process_file("asample.txt")
process_file("A-small-attempt1.in")
#process_file("A-large.in")