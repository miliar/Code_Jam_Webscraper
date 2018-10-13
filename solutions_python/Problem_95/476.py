#!/usr/bin/python2.7 -tt

"""
Shikhar Srivastav
Google Code Jam 2012
Problem 1
"""

def main():


#	s1="""ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv"""
#	s2="""our language is impossible to understand
#there are twenty six factorial possibilities
#so it is okay if you want to just give up"""
	"""
	gdict={}
	whitespace=" \n\r"
	for c1,c2 in zip(s1,s2):
		if(c1 not in whitespace):
			if not gdict.has_key(c1):
				gdict[c1]=c2
	gdict['q']='z'
	gdict['z']='q'
	"""
	gdict={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	f=open("inp.txt")
	ans=[]
	for line in f:
		s=""
		for char in line:
			if char != '\n':
				s+=gdict[char]
		ans.append(s)
	for i in range(len(ans)):
		print "Case #"+str(i+1)+": "+ans[i]


if __name__=='__main__':
	main()
