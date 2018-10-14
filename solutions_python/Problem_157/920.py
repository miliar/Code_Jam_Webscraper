import sys
sys.setrecursionlimit(100000)

i_then = {	"i": "-1",
			"j": "k",
			"k": "-j" }

j_then = {	"i": "-k",
			"j": "-1",
			"k": "i" }
			
k_then = {	"i": "j",
			"j": "-i",
			"k": "-1" }
			
one_then = {	"i": "i",
				"j": "j",
				"k": "k" }
				
mi_then = {	"i": "1",
			"j": "-k",
			"k": "j" }

mj_then = {	"i": "k",
			"j": "1",
			"k": "-i" }
			
mk_then = {	"i": "-j",
			"j": "i",
			"k": "1" }
			
mone_then = {	"i": "-i",
				"j": "-j",
				"k": "-k" }

				
def traverse(a, b):
	if a == "i":
		return i_then[b]
	if a == "j":
		return j_then[b]
	if a == "k":
		return k_then[b]
	if a == "1":
		return one_then[b]
	if a == "-i":
		return mi_then[b]
	if a == "-j":
		return mj_then[b]
	if a == "-k":
		return mk_then[b]
	if a == "-1":
		return mone_then[b]

line = ""
index_i = 0
index_j = 0
index_k = 0

def find_i(index, now):
	ans = traverse(now, line[index])
	# print
	# print find_i
	# print "\tindex", index,
	# print "\tnow", now,
	# print "line[index]", line[index],
	# print "\tans", ans,
	if index + 1 < len(line):
		if ans == "i":
			index_i = index
			find_j(index + 1, "1", index_i)
		else:
			find_i(index + 1, ans)
	else:
		print "NO"

def find_j(index, now, index_i):
	ans = traverse(now, line[index])
	# print
	# print find_j
	# print "\tindex", index,
	# print "\tnow", now,
	# print "line[index]", line[index],
	# print "\tans", ans,
	if index + 1 < len(line):
		if ans == "j":
			index_j = index
			find_k(index + 1, "1", index_j, index_i)
		else:
			find_j(index + 1, ans, index_i)
	else:
		# find_i(index_i + 1, "i")
		print "NO"

def find_k(index, now, index_j, index_i):
	ans = traverse(now, line[index])
	# print
	# print find_k
	# print "\tindex", index,
	# print "\tnow", now,
	# print "line[index]", line[index],
	# print "\tans", ans,
	if index + 1 == len(line):
		if ans == "k":
			index_k = index
			print "YES"
		else:
			print "NO"
	elif index + 1 < len(line):
		find_k(index + 1, ans, index_j, index_i)
	else:
		# find_j(index_j + 1, "j", index_i)
		print "NO"
		
cases = input()
		
for t in range( 1, cases + 1 ):
	lx = raw_input()
	l, x = lx.split()

	line = raw_input()
	line = line * int(x)
	# print line
	line = list(line)
	
	print "Case #" + repr(t) + ":",
	find_i(0, "1")
	