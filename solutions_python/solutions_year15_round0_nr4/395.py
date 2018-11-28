# -*-coding:utf8 -*
from parsing import TextGen
infile = "d.in"
outfile = "d.out"

########################
def cutdiv(a, b):
    return -(-a // b) - 1

def algo2(size,rows,cols):
	if size >= 7: return False
	elif size == 1: return True
	elif ((rows % size) * (cols % size)) % size != 0: return False
	elif size == 2: return True
	else: return (rows >= (size-1) and cols >= (size-1))
	# elif size == 3: return (rows >= 2 and cols >= 2)
	# elif size == 4: return (rows >= 3 and cols >= 3)
	# elif size == 5: return (rows >= 4 and cols >= 4)
	# elif size == 6: return (rows >= 5 and cols >= 5)
	
def algo(inp):
	size = inp.int
	rows = inp.int
	cols = inp.int
	return "GABRIEL" if algo2(size,rows,cols) else "RICHARD"
	


########################

inp = TextGen(infile)
cases = inp.int
with open(outfile,'w') as outdata:
	for case in range(1, cases+1):
		outdata.write("Case #%d: %s\n" % (case, algo(inp)))
