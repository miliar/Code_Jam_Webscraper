
def check(dat):
	for i in range(4):
		w = "".join([ dat[j][i] for j in range(4) ])
		dat.append(w)
	w = "".join([ dat[j][j] for j in range(4) ])
	dat.append(w)
	w = "".join([ dat[j][4-1-j] for j in range(4) ])
	dat.append(w)
	
	#print dat
	
	finish = True
	
	for w in dat:
		x = w.count("X")
		o = w.count("O")
		t = w.count("T")
		
		if x + t == 4:
			return "X won"
		if o + t == 4:
			return "O won"
		
		if x + o + t < 4:
			finish = False

	if finish:
		return "Draw"
	else: 
		return "Game has not completed"

T = int(raw_input())


for n in range(T):
    dat = ["" for _ in range(4)]
    for i in range(4):
        dat[i] = raw_input()
    if n<T-1: dummy = raw_input()

    #print dat
    print "Case #%d: %s"  % (n+1, check(dat))