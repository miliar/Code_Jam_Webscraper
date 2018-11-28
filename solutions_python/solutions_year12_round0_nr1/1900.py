data = [[1 for i in xrange(26)] for j in xrange(2)]

def build_tab(s_in, s_out, dsf = ['' for i in xrange(26)]):
	global data
	if len(s_in) != len(s_out):
		print "error"
		return []
	else:		
		for i in xrange(len(s_in)):			
			if(s_in[i] != ' '):
				dsf[ord(s_in[i])-97] = s_out[i]
				data[0][ord(s_in[i])-97] = 0
				data[1][ord(s_out[i])-97] = 0
	return dsf

def discover_missing_links():
	tab = build_tab('y qe', 'a zo')
	tab = build_tab('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand', tab)
	tab = build_tab('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities', tab)
	tab = build_tab('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up', tab)

	for i in xrange(26):
		print chr(i+97), ': ', tab[i]
	
	print 'Unknown G: ',
	for i in xrange(26):
		if data[0][i] == 1:
			print chr(i+97), '; ', 

	print

	print 'Unknown E: ',
	for i in xrange(26):	
		if data[1][i] == 1:
			print chr(i+97), ';', 
		
	print
	# so there is only one missing link: z -> q
	
def build_dict(s_in, s_out, dsf = {}):
	n = len(s_in)
	if len(s_out) != n:
		return dsf
	for i in xrange(len(s_in)):
		dsf[s_in[i]] = s_out[i]
	return dsf
	
def tlate(s, D):
	sret = ''
	for i in s:
		sret += D[i]
	return sret
	
	
def init():
	#Build Dictionary
	D = build_dict('y qez', 'a zoq')
	D = build_dict('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand', D)
	D = build_dict('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities', D)
	D = build_dict('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up', D)
	
	#Get Inputs and Translate Them
	fin = open('A.in', 'r')
	L = fin.readlines()
	fin.close()
	
	OL = []			
	for i in xrange(1,1+int(L[0])):
		OL.append('Case #' + str(i) + ': ' + tlate(L[i].strip().lower(), D) + '\n')
		
	fout = open('A.out', 'w')
	fout.writelines(OL)
	fout.close()
	
init()	
