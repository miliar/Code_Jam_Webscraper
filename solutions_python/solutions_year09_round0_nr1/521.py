import sys

words = []

def match_substring(start, index):
    global K, tok
#    print "  "*index, "finding", start, index
    if index >= L:
#	print "  "*index, "found",
	for w in words:
	    if start == w:
#		print start, index, 
		K += 1
#	print
	return
    t = tok[index]
    if len(t) == 1:
#	print "  "*index, "xxxxxxxxxxxxxxxxxxx"
	new_start = start + t
	for w in words:
	    if w.startswith(new_start):
		match_substring(new_start, index+1)
		break
    else:
	for c in t:
	    new_start = start + c
#	    print "  "*index,"looking for", new_start, "in", c, "of", t
	    for w in words:
		if w.startswith(new_start):
		    match_substring(new_start, index+1)
		    break
# 	    print "  "*index,"end"


assert len(sys.argv) == 2
read  = open(sys.argv[1], "r")
write = open(sys.argv[1]+".out", "w")

L,D,N = read.readline().split()
L = int(L)
D = int(D)
N = int(N)

for d in range(D):
    words.append(read.readline().strip())
#print words

for n in range(N):
    line = read.readline().strip()
    # split token
    tok = []
    in_par=False
    t = ""
    for c in line:
	if in_par:
	    if c == ")":
		in_par = False
		tok.append(t)
		t = ""
	    else:
		t += c
	else:
	   if c == "(":
		in_par = True
	   else:
		tok.append(c)
    K = 0
#    print tok
    match_substring("", 0)
#    print 
    write.write("Case #%s: %s\n" % (n+1, K))
    print "Case #%s: %s" % (n+1, K)

