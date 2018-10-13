import sys
from math import *
from string import *

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

def ice():
    nn = int((file.readline().split())[0])
    m = int((file.readline().split())[0])
    a = []
    for i in range(m):
	a.append([])
	q = map(int,file.readline().split())
	np = q[0]
	r = q[1:]
	for j in range(np):
	    a[i].append([r[2*j],r[2*j+1]])
    print a
	
    return "0"

def crop():
    n, a, b, c, d, x0, y0, m = map(int,file.readline().split())
    pts = []
    x = x0
    y = y0
    pts.append([x0,y0])
    for i in range(1,n):
	x = (a*x+b)%m
	y = (c*y+d)%m
	pts.append([x,y])
    c = 0

    v = []
    for q in range(3):
	v.append([])
	for r in range(3):
	    v[q].append(0)
    
    for p in pts:
	px = p[0]%3
	py = p[1]%3
	#print px,py
	v[px][py] +=1

    print v

#    for i in range(3):
#	for j in range(3):
#	    c+= (v[i][j])*(v[i][j]-1)*(v[i][j]-2)/6
    
    for i in range(3):
	c+= v[i][1]*v[i][2]*v[i][0]
	c+= v[1][i]*v[2][i]*v[0][i]

    for i in range(3):
	c += v[i%3][0] * v[(i+1)%3][1] * v[(i+2)%3][2]
    
    for i in range(3):
	c += v[i%3][0] * v[(i-1)%3][1] * v[(i-2)%3][2]

#    print c

#    for i in range(len(pts)):
#	for j in range(i+1,len(pts)):
	    #for k in range(j+1,len(pts)):
	#	if (pts[i][0]+pts[j][0]+pts[k][0])%3 == 0 and (pts[i][1]+pts[j][1]+pts[k][1])%3 == 0:
#	    kx = (pts[i][0]+pts[j][0])%3
#		    c+=1
    return str(c)

def cropb():
    n, a, b, c, d, x0, y0, m = map(int,file.readline().split())
    pts = []
    x = x0
    y = y0
    pts.append([x0,y0])
    for i in range(1,n):
	x = (a*x+b)%m
	y = (c*y+d)%m
	pts.append([x,y])
    c = 0

    for i in range(len(pts)):
	for j in range(i+1,len(pts)):
	    for k in range(j+1,len(pts)):
		if (pts[i][0]+pts[j][0]+pts[k][0])%3 == 0 and (pts[i][1]+pts[j][1]+pts[k][1])%3 == 0:
		    c+=1
    return str(c)


def numsets():
    a, b, p = map(int,file.readline().split())

def grab():
    return int(file.readline())

def grabs():
    return map(int,file.readline().split())


def mt():
    k = int(file.readline())
    r = map(int,file.readline().split())
    n = r.pop(0)
    #print n, r
    sn = range(k)
    a = [0]*k
    c = 0
   # a[0] = 1
    i = 1
    cc = 0
    p=0
    d3ex = range(k)
    dex = sorted(d3ex)
    while i <=k:
#	p = 0
#	if k == i:
#	    while a[c] == 0:
#		c=(c+1)%k
#	else:
#	while p <= (i%(k-i+1)):
#	    c = (c+1)%k
#	    if a[c] == 0:
#		p+=1
#	    c = (c+1)%k
#	a[c]=i
	
	#cc = 0
#	if i*(i+1)/2 <= k:
#	    a[i*(i+1)/2-1] = i
#	    cc = i*(i+1)/2-1
#	else:
#	    rd = k-i+1
#	    v = i % rd
#	    if i ==6:
#		print rd,v,cc
#	    if v == 0:
#		v = rd
#	    pos = cc
#	    vv = 0
#	    while vv < v:
#		pos = (pos+1)%k
#		if a[pos] == 0:
#		    vv+=1
#	    a[pos] = i 
#	    cc = pos'''

	rd = k-i+1
	
	v = (p+i-1)%rd
#	print dex,a
	a[dex[v]] = i
	p = dex.index(dex[v])
	dex.remove(dex[v])
	
	i = i+1
  #  print k
#    print a
    s = ""
    for j in r:
	s += str(a[j-1]) + " "
    return s


def phone():
    p,k,l = grabs()
    fs = grabs()
    
    fs.sort()

    c = 0
    for i in range(l):
	c+=fs[l-i-1] * (i/k + 1)

    return str(c)



def removechars(str, chars):
    return str.translate(maketrans('',''),chars)

def milkshakes():
    def check():
	for i in range(len(table)):
	    p = 0
	    if table[i] == 1:
		continue
	    if table[i] == 0:
		return -2
	    if len(table[i]) == 0:
		return -3
	    cc = 0
	    for c in range(len(table[i])):
		#if table[i][c] != 0:
		 #   cc = 1
		  #  break
		if table[i][c] != 0:
		    cc += 1
		    p = c
	    if cc == 0:
		return -4
	    if len(table[i]) == 1 and table[i][0][1] == 1:
		return i
	    if cc == 1 and table[i][p][1] == 1:
		return i
	return -1

    n = grab()
    m = grab()

    table = []
    r = [0] * n
 #   print r

  #  print table

    for i in range(m):
	table.append([])
	g = grabs()
	t = g[0]
	for j in range(t):
	    table[i].append([g[2*j+1],g[2*j+2]])
#    print r

#    print n
 #   print table
    
    q = check()
#    print q
    while q >= 0:
#	print q
#	print table[q]
	qq = 0
	while table[q][qq] == 0:
	    qq+=1
	fl = table[q][qq][0]
	r[fl-1] = 1
	for k in range(len(table)):
	    if table[k] == 0 or table[k] <= 2:
		continue
	    else:
		for kk in range(len(table[k])):
		    if table[k] <= 2:
			continue
		    if table[k][kk] == 0:
			continue
		    if (table[k][kk][0] == fl and table[k][kk][1] == 1):
			table[k] = 1
		    elif (table[k][kk][0] == fl and table[k][kk][1] == 0):
			table[k][kk] = 0
#	print table, q, r
	q = check()

#    print q
    if q < -1:
	return "IMPOSSIBLE"
    else:
#	return str(r).translate(maketrans('',''),',/[]')
	return removechars(str(r),',[]')


#    print table
 #   return "0"

# numbers

def h2b(s):
    oo = ""
    for ii in s:
        if ord(ii) >= ord('0') and ord(ii) <= ord('9'):
            j = (ord(ii)-ord('0'))
        else:
            if ord(ii.lower()) >= ord('a') and ord(ii.lower()) <= ord('f'):
                j = (ord(ii.lower())-ord('a') + 10)
        for v in range(4):
            if j/2**(3-v) % 2 == 1:
                oo += '1'
            else:
                oo += '0'
    return oo

def h2d(s):
    return b2d(h2b(s))

def d2b(s):
    return h2b(d2h(s))

def d2h(n):
    k = hex(n)
    return k[2:len(k)]

def b2h(s):
    return d2h(b2d(s))

def b2d(s):
    kk = 0
    for i in range(len(s)):
        j = len(s) - 1 - i
        if s[j] == '1':
            kk += 2**i
    return kk


def exponent():
    def mul(x):
	xx = x
	bn = d2b(x)
	p = [1,0,0,1]
#	print bn
	for i in range(len(bn)):
	    if bn[::-1][i] == '1':
		pp = t[i]
		p = [p[0]*pp[0]+p[1]*pp[2],p[0]*pp[1]+p[1]*pp[3],p[2]*pp[0]+p[3]*pp[2],p[2]*pp[1]+p[3]*pp[3]]
#		print p

	return p
##	print x
#	q = int(floor(log(x)/log(2))) +1
#	if q == floor(q):
	    
#	p = t[q-1]
#	p = [1,0,0,1]
#	xx = x 
#	print xx,q
#	while xx > 0 and q > 0:
#	    q-=1
#	    xx = x - 2**q
	#    print xx,q
	  #  q-=1
	 #   if (xx  - (2**q)) >= 0:
	#	pp = t[q-1]
		
	#	print q
	#	xx -= (2**q)
	 #   q-=1
		
#	    q-=1
            
    n = grab()
    a, b, c, d = 3, 5, 1, 3
    
    
    t = [[a,b,c,d]]
    e = int(floor(log(n)/log(2))) + 1
    for i in range(e):
	aa = t[i][0]
	bb = t[i][1]
	cc = t[i][2]
	dd = t[i][3]
	
	aaa = aa*aa + bb*cc
	bbb = aa*bb + bb*dd
	ccc = cc*aa + dd*cc
	ddd = cc*bb + dd*dd
	t.append([aaa,bbb,ccc,ddd])
    
    m = mul(n-1)
 #   print n-1,m
    out = ((m[0]*3)+m[1])%1000
    o = (m[2]*3+m[3])
    out += int(ceil(o*sqrt(5))) -1
    #return str(out)
    return str(1000+(out%1000))[1:4]
    

def ugly():
    st = file.readline()[:-1]
    #print len(st), st
    a = []
    aa = []

    for i in range(len(st)):
	a.append([])
	aa.append([])
	for j in range(210):
		#p = int(st[0])
		a[i].append(0)
		aa[i].append(0)
	if i==0:
	    p = int(st[0])
	    a[i][p]=1
	else:
	    for j in range(210):
		#positives and zero
		numc = (j*10+int(st[i]))%210
		a[i][numc]+= a[i-1][j]
		numm = (j-int(st[i]))
		if numm < 0:
		    numm = (-numm)%210
		    aa[i][numm]+=a[i-1][j]
		else:
		    numm = numm%210
		    a[i][numm]+=a[i-1][j]
		a[i][numm]+= a[i-1][j]
		nump = (j+int(st[i]))%210
		a[i][nump]+= a[i-1][j]
		#negatives
		numc = -j*10+int(st[i])
		if numc >=0:
		    numc = numc%210
		    a[i][numc]+=aa[i-1][j]
		else:
		    numc = (-numc)%210
		    aa[i][numc]+=aa[i-1][j]
		numm = (-(-j-int(st[i])))%210
		aa[i][numm]+= aa[i-1][j]
		nump = -j+int(st[i])
		if nump >=0:
		    nump = nump%210
		    a[i][nump] += aa[i-1][j]
		else:
		    nump = (-nump)%210
		    aa[i][nump]+=aa[i-1][j]
    
    ct = 0
    for j in range(210):
	if j%2 == 0 or j%3 == 0 or j%5 == 0 or j%7 == 0:
	    ct+=a[len(st)-1][j]

    for j in range(210):
	if j%2 == 0 or j%3 == 0 or j%5 == 0 or j%7 == 0:
	    ct+=aa[len(st)-1][j]

    return str(ct)
    
#    return "0"



def stuff():
    def evaluate():
	r =  (range((m-1)/2))[::-1]
	#print r
	for i in r:
	#    print i
	    if itree[i][0] == 1:
		tree[i] = tree[2*(i+1)-1] and tree[2*(i+1)-1+1]
	#	print i
	    else:
		tree[i] = tree[2*(i+1)-i] or tree[2*(i+1)-1+1]
	#	print i

	return int(tree[0])

  #  def change():
	

  #  n = 0
    nc = 0
    #print file.readline()
    #print file.readline()
    m,v = grabs()
    itree = []
    tree = []
    for i in range((m-1)/2):
	g,c = grabs()
	if c == 1:
	    nc+=1
	itree.append([g,c])
	tree.append(0)
    for i in range((m+1)/2):
	leaf = grab()
	leaf = (leaf == 1)
	tree.append(leaf)

    for n in range(nc + 1):
	if evaluate() == v:
	    return n
	else:
	    if change():
		return "3"
	    else:
		return "IMPOSSIBLE"
#	    for o in range((m-1)/2):
	#	if itree[o][1] == 1:
		#    if change(o) == 1:
			
    
   # return "IMPOSSIBLE"

#    print tree
    #for (
    #return str(evaluate())
 #   print evaluate()
  #  print tree
   # print itree
    #return "0"
	
#    return "0"

def star():
    t = grab()
    x = []
    y = []
    z = []
    p = []
    for i in range(t):
	xx, yy, zz, pp = grabs()
	x.append(xx)
	y.append(yy)
	z.append(zz)
	p.append(pp)
    xa = 0
    ya = 0
    za = 0
    

    print x,y,z,p

    return "0"

# from http://snippets.dzone.com/posts/show/753
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def rle():
    def ct(ii):
	ctt = 0
#	v = []
#	for m in range(len(perms)):
#	    v.extend(perms[m][i])
#	v.flatten()
#	v.append('0')
	#print v
	tabl[ii].append(0)
	for r in range(len(tabl[0])-1):
	    if tabl[ii][r]!=tabl[ii][r+1]:
		ctt+=1
#	if ctt == 9:
#	    print v
	return ctt

    k = grab()
    ss = removechars(file.readline(),'\n')
    ll = len(ss)
    nn = ll/k
    ps = []
    for j in all_perms(range(k)):
	ps.append(j)

    tabl = []
    for i in range(len(ps)):
	tabl.append([])
	perm = ps[i]
	for j in range(nn):
	    subs = ss[j*k:j*k+k]
	    for jj in range(k):
		tabl[i].append(subs[perm[jj]])

 #   print tabl
	#for j in all_perms(list(ss[i:i+k])):
	#    perms[i].append(j)
#	print d.str()
	#perms.append(d)
	#perms.append(all_perms(ss[i:i+k]))

    cc = 1000000000000

    x = len(ps)
    for i in range(x):
	cc = min(cc,ct(i))

   # print perms

    
    
    return str(cc)

for arg in sys.argv:
    file = open(arg)

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
   # s += ugly()
    s+= rle()
   # s+= stuff()
   # s+=star()
#s += exponent()
   # s+= phone()
#    s += crop()	
   # s+= numsets()
    print s
