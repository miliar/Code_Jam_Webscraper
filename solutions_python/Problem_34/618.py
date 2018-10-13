import sys
import string

words = []
wordbank = []
####################
fin = open(sys.argv[1])
out = open("alienout.txt", "w")

ntokens, nwords, ncases  = [int(x) for x in fin.readline().split()]

for w in range(nwords):
	words.append( fin.readline().rstrip() )

wordbank = words[:]

for c in range(ncases):
	words = wordbank[:]
	intro = "Case #%d: " % (c+1)
	#print intro
	out.write(intro)
	
	counter = 0
	s = fin.readline()
	#print s
	index = 0
	pool = []
	#print words
	while len(s)>0:
		#print "\n#######################################\n"
		#print "lens: "+str(len(s))
		#print "s: "+str(s)
		pool = []
		first = s[0]
		s = s[1:]
		#encountered parens, get letters in parens
		if first == "(":
			#print "with parens index="+str(index)
			first = s[0]
			s = s[1:]
			while first != ")":
				pool.append(first)
				first = s[0]
				s = s[1:]
			kill = []
			for i in range(len(words)):
				#print "if its index letter isn't in pool, it's removed"
				w = words[i]
				if w[index] not in pool:
					"removing word"
					kill.append(i)
			#print kill
			
			words2 = words[:]
			for i in kill:
				#print i
				words.remove(words2[i])
			index += 1
		else: #encountered letter
			#print "no parens index="+str(index)
			for w in words:
				#print "w: "+str(w)
				#print "index: "+str(index)
				#print "first: "+str(first)
				if w[index] != first:
					words.remove(w)
			index += 1
		s = s.rstrip()
		
	final = str(len(words))
	#print final
	out.write(final+"\n")