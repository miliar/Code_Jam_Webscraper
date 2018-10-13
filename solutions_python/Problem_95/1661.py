other_tongue = open("A-small-attempt0.in", 'r')
my_mouth = open("out.txt", 'w')
print other_tongue.readline()
saliva = other_tongue.readlines()
print saliva
other_tongue.close()
mono = {"a" : "y", "b" : "h", "c": "e", "d" : "s", "e" : "o", "f":'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
MONO = ''
for virion in mono.keys():
	MONO += virion.upper()
my_tongue = ''
mouths = 0
for drop in saliva:
	mouths+=1
	my_tongue = 'Case #%d: ' %(mouths)
	for molec in drop:
		if molec in mono.keys():
			my_tongue += (mono[molec])
		elif molec in MONO:
			my_tongue += (mono[molec.lower()].upper())
		else:
			my_tongue += (molec)
	print my_mouth
	my_mouth.write(my_tongue)
my_mouth.close()



