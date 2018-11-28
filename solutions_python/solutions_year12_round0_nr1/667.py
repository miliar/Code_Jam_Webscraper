#!/usr/bin/python3

rosetta = {
"y qee":"a zoo",
"ejp mysljylc kd kxveddknmc re jsicpdrysi": "our language is impossible to understand",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd": "there are twenty six factorial possibilities",
"de kr kd eoya kw aej tysr re ujdr lkgc jv": "so it is okay if you want to just give up"
}

def analysis(r):
	"""
	Read the file and contruct a mapping
	"""
	
	base = " abcdefghijklmnopqrstuvwxyz"
	mp = dict()
	for c in base:
		mp[ord(c)] = None
	# Add the space as known
	mp[ord(" ")] = ord(" ")
	
	for googlish, normal in r.items():
		
		for j in range(len(googlish)):
			g = ord(googlish[j])
			c = ord(normal[j])
			if mp[g] is None:
				mp[g] = c
			elif mp[g]!=c:
				print("Somiething weird...")
	
	# See how many are missing
	miss = sum([ x is None for x in mp.values() ])
	if miss==1:
		# Build the inverse map
		invtxt = base
		for k, v in mp.items():
			if v is None:
				unmapped = k
			else:
				invtxt = invtxt.replace(chr(v), "")
		mp[unmapped] = ord(invtxt)
		return mp
	elif miss>1:
		print("Bad Luck!")
		return None
	else:
		return mp


import sys

# Generate first the Goglish map
Googlish = analysis(rosetta)

if Googlish is None:
	print("Failure to solve the map :(")
	sys.exit(1)

# Now read the input and decode it
if len(sys.argv)<2:
	fd = sys.stdin
else:
	fd = open(sys.argv[1],"r")


T = int(fd.readline().strip())
	
for i in range(T):
	words = fd.readline().strip()
	human = words.translate(Googlish)
	print("Case #%d: " % (i+1) + human)

fd.close()



