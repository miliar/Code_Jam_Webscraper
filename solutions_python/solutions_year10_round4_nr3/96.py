# -*- coding: utf-8 -*-
from operator import attrgetter
fname = "C-small-attempt0"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

class rectangle(object):
    def __init__(self, X1, Y1, X2, Y2):
	self.X1 = X1
	self.X2 = X2
	self.Y1 = Y1
	self.Y2 = Y2
    def __repr__(self):
	return "rectangle(" +str(self.X1)+","+str(self.Y1)+","+str(self.X2)+","+str(self.Y2)+")"

for caseno in range(numcases):
  R = gcj_read()[0]
  rectangles = []
  r_ind_death_times = []
  for i in range(R):
    X1, Y1, X2, Y2 = gcj_read()
    rectangles.append(rectangle(X1, Y1, X2, Y2))
  rectangles.sort(key=attrgetter('X1','Y1'))
  contigs = []
  for rt in rectangles:
      incontig = -1
      for cnum, contig in enumerate(contigs):
	  for cp in contig:
	      if (rt.X1 <= cp.X2+1) and (((rt.Y2 >= cp.Y1-1) and (rt.Y1 <= cp.Y2+1))\
	      and not((rt.X1,rt.Y1) == (cp.X2+1, cp.Y2+1))):
		contig.append(rt)
		if incontig > -1:
		    contigs[incontig] += contig
		    contig =  []
		else:
		    incontig = cnum
		break
      if incontig == -1:
	  contigs.append([rt])
  ctg_ttd = []
  for contig in contigs:
    print contig
    NWdist_min = max([r.X1 for r in contig]) + max([r.Y1 for r in contig]) + 1
    for rt in contig:
	NWdist = rt.X1 + rt.Y1
	if NWdist < NWdist_min:
	    wavestart = (rt.X1, rt.Y1)
	    NWdist_min = NWdist
    waveend = (max([r.X2 for r in contig]), max([r.Y2 for r in contig]))
    print wavestart, waveend
    ctg_ttd.append((waveend[0] - wavestart[0]) + (waveend[1] - wavestart[1]) + 1)
  ttd = str(max(ctg_ttd))
  fout.write("Case #"+str(caseno+1)+": "+ ttd +"\n")

fin.close()
fout.close()