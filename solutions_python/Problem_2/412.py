import sys
def main():
	filename=sys.argv[1]
	f=open(filename,'r')
	fout=open('boutput.txt','w')
	tcCount = int(f.readline())
	for i in range(tcCount):
		turnaround = int(f.readline())
		trips = f.readline()
		tlist = trips.split()
		nab = int(tlist[0])
		nba = int(tlist[1])
		#print 'trips =', nab, nba
		# read trips from A to B
		tripab = []
		tripba = []
		for j in range(nab):
			str = f.readline()
			tripab.append(str.split())
		for j in range(nba):
			str = f.readline()
			tripba.append(str.split())
		
		aready = []
		ago = []
		bready = []
		bgo = []
		for ab in tripab:
			ago.append(converttonum(ab[0]))
			bready.append(converttonum(ab[1],turnaround,0))
		for ba in tripba:
			bgo.append(converttonum(ba[0]))
			aready.append(converttonum(ba[1],turnaround,0))
			
		aready.sort()
		bready.sort()
		ago.sort()
		bgo.sort()
		#print aready, ago
		#print bready, bgo
		
		acount = 0
		while len(ago) > 0:
			train = ago.pop(0)
			if len(aready) == 0:
				acount = acount+1
				continue
			else:
				avail = aready[0]
				if (avail <=train):
					aready.pop(0)
				else:
					acount = acount + 1

		bcount = 0
		while len(bgo) > 0:
			train = bgo.pop(0)
			if len(bready) == 0:
				bcount = bcount+1
				continue
			else:
				avail = bready[0]
				if (avail <=train):
					bready.pop(0)
				else:
					bcount = bcount + 1
		
		outstr = 'Case #%d: %d %d' % ((i+1), acount, bcount)
		print outstr
		fout.write(outstr+'\n')
	f.close()
	fout.close()

def converttonum(str, turn=0, addturn=1):
	strlist = str.split(':')
	hh = int(strlist[0])
	mm = int(strlist[1])
	if addturn == 0:
		newmm = mm+turn
		mm = newmm % 60
		hh = hh + newmm / 60
	
	ttime = (hh*100)+mm
	return ttime
	
	
main()
	
	
