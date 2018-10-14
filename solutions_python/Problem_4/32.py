import sys
from math import *

MAX = 1000000000

def switches():
    ns = int(file.readline())

    ses = []
    for j in range(ns):
	ses.append(file.readline()[:-1])

    #print ses,
    nq = int(file.readline())

    qus = []
    for k in range(nq):
	qus.append(file.readline()[:-1])

#    print ses, qus

	#DYNAMIC PROGRAMMING
    table = []
    for jj in range(nq):
	table.append([])
	for kk in range(ns):
	    if qus[jj] == ses[kk]:
		conf = 1
	    else:
		conf = 0
	    table[jj].append(conf)

 #   print table
    if nq == 0:
	return "0"
    score = [[]]
    for m in range(ns):
	score[0].append(table[0][m])
    
    for v in range(1,nq):
	score.append([])
	for x in range(ns):
	    if table[v][x] == 1:
		score[v].append(MAX)
		
	    else:
		cc = MAX
		for p in range(ns):
		    if p == x:
			ad = 0
		    else:
			ad = 1
		    cc = min(cc, score[v-1][p] +ad)
		score[v].append(cc)
    #return str(score)
    scc = MAX
    for kkk in range(ns):
	scc = min(scc,score[nq-1][kkk])

    return str(scc)
	

    #print table
#    for m in range(nq):
	

#    return "0"


def ar(x1,x2,y,r):
    def integ(x):
	return .5 * asin(x) + .5 * x * sqrt(1-x**2)

    return r**2 * (integ(x2/r) - integ(x1/r)) - y * (x2-x1)

def prob():
    f, rr, t, r, g = map(float,file.readline().split())
   # print [f, rr, t, g]
    total = pi * rr**2 / 4.0
    #print total
    count = 0.0
    r0 = rr-t-f
    ltt = g - 2*f
    area = ltt**2
    if f > g/2:
	return "1.0000000"

    x = r+f
    while (x < r0):
	y = r + f
	while (y < r0):
	    xx = x + ltt
	    yy = y + ltt
	    p = sqrt(x**2 + y**2)
	    q = sqrt(xx**2 + yy**2)
	    
	    if p >= rr-t-f:
		count += 0
	    else:
		if q <= rr-t-f:
		    count += area
		else:
		    #count += (g-2*f)**2/2
		    ty = sqrt(r0**2-x**2)
		    tyy = sqrt(r0**2-xx**2)
		    tx = sqrt(r0**2 -y**2)
		    txx = sqrt(r0**2-yy**2)
		    
		    if (ty < yy):
			
			if (tyy > y): #A
			    #count += ((ty+tyy)/2 -y) / (yy-y) * area
			   # print ar(0,1,0,1)*4
			    count += ar(x,xx,y,r0)

			else: #B
#			    count += .25 * area
			    count += ar(x,tx,y,r0)
		    else:
			if (tyy > y): #C
#			    count += .75 * area
			    count += ar(txx,xx,y,r0) + (yy-y)*(txx-x)
#			    count += ar(x,xx,y,r0)-ar(x,txx,yy,r0)
			else: #D
			    count += ar(y,yy,x,r0)
#			    count += .5 * area

	    y += g + 2*r
	x +=  g + 2*r

#    y = r+f+g-2*f

 #   while 
    qqq = (total-count)/total
    return str(qqq)
#    if qqq < 1e-7:
#	return "0.000000"
#    else:
#	return str(qqq)


def train():
    t = int(file.readline())
    na, nb = map(int, file.readline().split())

    #print [t,na,nb]

    trips = []
    for i in range(na+nb):
	#print file.readline()
	tt1, tt2 = file.readline().split()
	t1 = 60*int(tt1[0:2]) + int(tt1[3:5])
	t2 = 60*int(tt2[0:2]) + int(tt2[3:5]) # + t
	if i < na:
	    stat = 0
	else:
	    stat = 1

	trips.append([t1,t2,stat])
    trips.sort()

#    mt = 0
    trains = []
    act = 0
    bct = 0
    for x in trips:
	assigned = 0
	ck = 0
	for iy in range(len(trains)):
#	    if y[0]
	    y = trains[iy]
	    if y[2] != x[2] and x[0] >= y[1] + t:
		trains[iy] = x
		assigned = 1
		break
	if assigned == 0:
	    trains.append(x)
	    if x[2] == 0:
		act += 1
	    else:
		bct +=1
#	    trains.append([x[2],x])
	

  #  print trains

   # print len(trains), act, bct
    
    #print trips
	
	
#	print t1, t2, tt1, tt2
	

    return str(act) + " " + str(bct)

def alph():
    nn = int((file.readline().split())[0])
#    for i in range(nn):
    q = map(int,file.readline().split())
    r = map(int,file.readline().split())
    q.sort()
    r.sort()
    v = 0
    for p in range(nn):
	v+= q[p]*r[nn-p-1]
#    table = []
 #   for jj in range(nn):
#	table.append([])
#	for kk in range(nn):
	#    if qus[jj] == ses[kk]:
	#	conf = 1
	 #   else:
	#	conf = 0
#	    table[jj].append(MAX)
    #na, nb = map(int, file.readline().split())

 #   for jjj in range(nn):
#	for kkk in range(nn):
#	    table

#    print ta

    return str(v)

for arg in sys.argv:
    file = open(arg)

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += alph()	
#    s += train()
    print s
