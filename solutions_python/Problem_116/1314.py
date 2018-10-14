import re
text = open("A.in", "rt").readlines()
outfile = open("A.out", "wt")
tests = int(text[0])

lines = 0
offset = 1 
for test in range(tests):
    lines = 4
    ma = []
    mal = []
    full = ""
    for line in range(lines):
        lm = text[offset+line].strip()
	ma.append(list(lm))
	mal.append(lm)
	full += lm
	# print "\t", line, ":", ma

    diag1 = ""
    diag2 = ""
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""
    for k in range(4):
        diag1 += ma[k][k]
        diag2 += ma[k][3-k]
        col1 += ma[k][0]
	col2 += ma[k][1]
	col3 += ma[k][2]
	col4 += ma[k][3]
    mal.append(diag1)
    mal.append(diag2)
    mal.append(col1)
    mal.append(col2)
    mal.append(col3)
    mal.append(col4)
    # print mal

    winner = None
    result = None
    for s in mal:
        if re.match("[OT]{4}", s) is not None:
	    winner = "O"
	elif re.match("[XT]{4}", s) is not None:
	    # print "X:", s
	    winner = "X"
    if winner is not None:
        result = winner + " won"
    else:
	if re.search(r"\.", full) is None:
	   result = "Draw"
	else:
	   result = "Game has not completed"
    print "Case #", test+1, ":", result
    outfile.write("Case #%s: %s\n" % (test+1, result))
    offset = offset + lines + 1
    



