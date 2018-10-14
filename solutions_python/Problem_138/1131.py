from __future__ import division
import numpy as np

def war(nb, ken, naomi):
	npoints = 0
	for i in np.arange(nb):
		nplay = min(naomi)
		kplay = kenplay(nplay, ken)
		if nplay > kplay:
			npoints += 1
		ken = np.delete(ken, np.where(ken == kplay)[0])
		naomi = np.delete(naomi, np.where(naomi == nplay)[0])
	return npoints

def deceitWar(nb, ken, naomi):
	npoints = 0
	kens = np.sort(ken)
	naomis = np.sort(naomi)
	for i in np.arange(nb):
		if kens[0] < naomis[0]:
			kens = kens[1:]
			naomis = naomis[1:]
			npoints += 1
		else:
			nplay = naomis[0]
			ntold = max(kens) - .0000001
			kplay = kenplay(ntold, ken)
			if nplay > kplay:
				npoints += 1
			kens = np.delete(kens, np.where(kens == kplay)[0])
			naomis = np.delete(naomis, np.where(naomis == nplay)[0])
	return npoints

def kenplay(n, ken):
	if(len(ken[ken > n]) == 0):
		return min(ken)
	else:
		return np.min(ken[ken > n])


filen = 'in'
with open(filen) as f:
	content = f.readlines()
content = [i.strip() for i in content]

testn = 1
for i in np.arange(1, len(content), 3):
	nblocks = int(content[i])
	naomi = np.array([float(i1) for i1 in content[i + 1].split(" ")])
	ken = np.array([float(i1) for i1 in content[i + 2].split(" ")])
	print "Case #%d: %d %d" % (testn, deceitWar(nblocks, ken, naomi), war(nblocks, ken, naomi))
	testn += 1

