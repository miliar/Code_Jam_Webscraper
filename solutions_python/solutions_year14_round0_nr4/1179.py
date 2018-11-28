import pdb
import sys
import getopt
from collections import defaultdict

def moveN(naomi):
	naomi.sort()
	if (len(naomi) == 1):
		retval = [naomi[0], []]
	if (len(naomi) > 1):
		retval = [naomi[0], naomi[1:]]
	return retval

def optiKen(wn, ken):
	ken.sort()
	if (len(ken) == 1):
		retvalk = [ken[0], []]
	else:
		inds = [x[0] for x in enumerate(ken) if x[1] > wn]
		if (len(inds) == 0):
			retvalk = [ken[0], ken[1:]]
		else:
			vals = ken[0:inds[0]] + ken[inds[0]+1:]
			retvalk = [ken[inds[0]], vals ] 
	return retvalk

def dmoveN(naomi, ken):
	naomi.sort()
	ken.sort()
	if (len(naomi) == 1):
		retval = [naomi[0], []]
	else:
		if (min(naomi) < min(ken)):
			retval = [(max(ken) - 1e-5), naomi[1:]]
		if (min(naomi) > min(ken)):
			retval = [(max(ken) + 1e-5), naomi[1:]]
	return retval


def War(arg2, flag):
	num_weights = arg2[0][0]
	naomi = arg2[1]
	naomi.sort()
	ken = arg2[2]
	ken.sort()
	nwins = 0
	for i in range(num_weights):
		if (flag  == 0):
			retwn = moveN(naomi)
		else:
			retwn = dmoveN(naomi, ken)
		naomi = retwn[1]
		retwk = optiKen(retwn[0], ken)
		ken = retwk[1]
		if (retwn[0] > retwk[0]):
			nwins += 1
	return nwins

def wargames(arg2, ind):
	# normal war
	t1 = War(arg2, 0)
	# deciteful war
	t2 = War(arg2, 1)
	otxt = "Case #"+str(ind)+": "+str(t2)+" "+str(t1)
	return otxt


def main():
	fname = sys.argv[1]
	count = 0
	ind = 0
	innloop = 0
	fh = open(fname, 'r')
	outname = "/Users/adityajitta/Desktop/output4L.txt"
	fh1 = open(outname, 'w')
	for l in fh:
		if (count == 0):
			tl = l.strip()
		if (count > 0):
			l=l.strip()
			if(innloop == 0):
				ind += 1
				val = int(l.strip())
				arg2 = defaultdict(list)
				arg2[innloop] = [val]
			if (0 < innloop < 3):
				arg2[innloop] = map(float,l.strip().split())
			innloop += 1
			if (innloop == 3):
				out_txt = wargames(arg2, ind)
				print >>fh1, out_txt
				innloop = 0
		count += 1
	fh.close()
	fh1.close()


if __name__ == '__main__':
	main()
