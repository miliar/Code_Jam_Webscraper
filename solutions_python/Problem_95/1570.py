import os

os.chdir("/Users/Junzologies/Dropbox/Code Jam/Qualification 2012/A")

filer=open("A-small-attempt0.in","r")
filew=open("A-small-attempt0.out","w")

googlerese={"a":"y","b":"h","c":"e","d":"s","e":"o","f":"c","g":"v","h":"x","i":"d","j":"u","k":"i","l":"g","m":"l","n":"b","o":"k","p":"r","q":"z","r":"t","s":"n","t":"w","u":"j","v":"p","w":"f","x":"m","y":"a","z":"q"," ":" "}

cases=int(filer.readline())

for count in xrange(cases):
	filew.write("Case #"+str(count+1)+": ")
	line=filer.readline().strip("\n")
	for char in line:
		filew.write(googlerese[char])
	filew.write("\n")
filer.close()
filew.close()