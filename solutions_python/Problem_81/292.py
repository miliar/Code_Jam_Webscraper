#!/usr/bin/python

# count number of appearances of char c in list s
def count(c, s):
	res = len([i for i in s if i==c])
	return res
	
T = int(raw_input())

for t in range(T):
	N = int(raw_input())
	NN = range(N)
	lines = []
	for n in NN:
		lines.append(raw_input())
	wpl = []
	owpl = []
	for n in NN:
		#print lines[n]
		wp = float(count("1",lines[n]))/len(lines[n].replace(".",""))
		#print wp
		wpl.append(wp)
		opps = [lines[i] for i in NN if i != n and lines[i][n] != "."]
		#print n, "---", opps
		owp = 0
		for o in opps:
			o = [o[i] for i in NN if (i != n) and (o[i] != ".")]
			#print "o --- ", o , float(count("1",o))/len(o)
			owp += float(count("1",o))/len(o)
		owp = owp/len(opps)
		owpl.append(owp)
	print "Case #%d:" % (t+1)
	for n in NN:
		temp = [owpl[i] for i in NN if i != n and lines[i][n] != "."]
		oowp = sum(temp)/len(temp)
		#print wpl[n], owpl[n], oowp
		print (0.25*wpl[n] + 0.50*owpl[n] + 0.25*oowp)
		#print wpl[n], owpl[n], oowp
		