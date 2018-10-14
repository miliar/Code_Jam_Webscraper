# -*- coding: utf-8 -*-

def fileopen( name ) :
	f = file( name )
	strings = f.read().split("\n")
	s = strings[0]
	if len(strings[len(strings) - 1]) == 0:
		del strings[len(strings) - 1]
	del strings[0]
	s = s.split()
	l = int(s[0])
	d = int(s[1])
	p = int(s[2])
	dict = strings[0:d]
	paterns = strings[d:]
	return ( l, dict, paterns)

def parsePatern( pat ):
	res = []
	c = ""
	for i in pat:
		if i == "(" and len(c) != 0:
			res.append(c)
			c = ""
		if( i == ")"):
			res.append( c )
			c = ""
			continue
		c += i
	if len(c) != 0:
		res.append(c)
	return res
def chek( pats, dict):
	count = 0
	patlen = 0
	for i in pats:
		if( i[0] == "("): patlen+=1
		else : patlen += len(i)
	for w in dict:
		#print w
		if( len(w) != patlen ):
			break
		k = 0
		c = True
		for p in pats:
			#print p
			if not c: break
			if( p[0] == "(" ) :
				#print w[k], k, p	
				if not w[k] in p:
					c = False
				k+=1
			else:
				tt = len(p)
				subs = w[k:k+tt]
				k+=tt
				if subs != p:
					#print "!!", subs, p
					c = False
		#print c
		if c: count += 1
	return count
	
						
if __name__ == "__main__":
	res = fileopen("input.txt")
	#print res
	index = 1
	out = open( "out.txt", "w")
	for i in res[2]:	
		pp = parsePatern(i)
		#print pp
		out.write("Case #" + str(index) + ": " + str(chek(pp,res[1] )) +"\n" )
		index +=1 
	