#!/usr/bin/python
import sys
#Whose turn is it, how far do they need to go. Can move in parallel but should press in serialization order.
debug=False
def debugop(s):
	global debug
	if debug:
		print s
f=open(sys.argv[1])
if len(sys.argv) > 2:
	if(sys.argv[2] == "y"):
		debug=True
tc=int(f.readline().strip())
for i in range(0,tc):
	l=f.readline().strip()
	if not l:
		continue
	o=[]
	b=[]
	moves = l.strip().split()[1:]
	debugop(moves)
	for j in range(0,len(moves),2):
		color=moves[j]
		button=moves[j+1]
		if(color=="O"):
			o.append((int(button),j))
		else:
			b.append((int(button),j))
	#o.sort()
	#b.sort()
	odir="+"
	bdir="+"
	debugop("o="+str(o)+"b="+str(b))
	olen=len(o)
	blen=len(b)
	oindex=0
	bindex=0
	opos=1
	bpos=1
	movecnt=0
	if olen == 0:
		o.append((3,len(moves)+2))
	if blen == 0:
		b.append((3,len(moves)+2))
	for k in range(0,len(moves),2):
		if o[oindex][1] == k:
			nmoves = abs(o[oindex][0]-opos)
			movecnt = movecnt + nmoves
			opos = o[oindex][0]
			if b[bindex][0] >= bpos:
				bpos = min(bpos + nmoves,b[bindex][0])
			else:
				bpos = max(bpos-nmoves,b[bindex][0])
		else:
			nmoves = abs(b[bindex][0]-bpos)
			movecnt = movecnt + nmoves
			bpos = b[bindex][0]
			if o[oindex][0] >= opos:
				opos = min(opos + nmoves,o[oindex][0])
			else:
				opos = max(opos-nmoves,o[oindex][0])		
		if opos == o[oindex][0] and o[oindex][1] == k:
			debugop("o pressed")
			oindex = oindex + 1 if oindex < olen-1 else oindex
			movecnt = movecnt + 1
			if b[bindex][0] >= bpos:
				bpos = min(bpos + 1,b[bindex][0])
			else:
				bpos = max(bpos - 1,b[bindex][0])
		if bpos == b[bindex][0] and b[bindex][1] == k:
			debugop("b pressed")
			bindex = (bindex + 1) if bindex < blen-1 else bindex
			movecnt = movecnt + 1
			if o[oindex][0] >= opos:
				opos = min(opos + 1,o[oindex][0])
			else:
				opos = max(opos-1,o[oindex][0])		
		debugop("opos=%d and bpos=%d" % (opos,bpos))
		debugop("movecnt=%d , k=%d" % (movecnt,k))
	print "Case #%d: %d" % ((i+1),movecnt)
		
		
	
	
		