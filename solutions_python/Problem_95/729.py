import sys, os
import os.path

def replace(filename):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	cypher   = ["y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"]
	f = open(filename, 'r')
	base = f.readlines()
	base = base[1:] #Remove received number, we really don't need it
	for i in range(len(base)):
		base[i] = base[i].replace("\n", "") #Line feed
		base[i] = base[i].replace("\r", "") #Carrier return
		for j in range(len(alphabet)):
			base[i] = base[i].replace(cypher[j],alphabet[j])
		base[i] = "Case #" + str(i+1) + ": "+ base[i].swapcase()
	r = open("Results1.txt", "w")
	for line in base:
		r.write("%s\n" % line)
	f.close()
	r.close()
	
if __name__ == "__main__":
	filename = sys.argv[1]
	replace(filename)