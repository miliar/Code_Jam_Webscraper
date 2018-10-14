import sys

mapping = {"e":"o","j":"u","p":"r"," ":" ","m":"l","y":"a","s":"n","l":"g","c":"e","k":"i","d":"s","x":"m","v":"p","n":"b","r":"t","i":"d","b":"h","t":"w","a":"y","h":"x","w":"f","f":"c","o":"k","u":"j","g":"v","z":"q","q":"z"}

i = 0

for line in sys.stdin:
	i += 1
	if i == 1: 
		continue
	c = ''
	for char in line[:-1]:
		c += mapping[char]
	print "Case #"+str(i-1)+": " +c