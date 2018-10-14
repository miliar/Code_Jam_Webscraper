import sys, os
import os.path

def shiftLeft(word):
	return word[1:]+word[0]

def shiftRight(word):
	return word[-1]+word[:-1]

def numbers(filename):
	f = open(filename, 'r')
	base = f.readlines()
	base = base[1:] #Remove received number, we really don't need it
	for i in range(len(base)):
		base[i] = base[i].replace("\n", "") #Line feed
		base[i] = base[i].replace("\r", "") #Carrier return
		# ########## LOGIC ##########
		total = 0
		minimum,maximum = base[i].split()
		for n in range(int(minimum), int(maximum) + 1):
			switches = len(minimum) -1 #How many shifts can there be before we return to the same number
			s = n
			pairs = [] #Cache found results, duplicate detection!
			while(switches >0):
				s = shiftLeft(str(s))
				if(int(s) > n and s >= minimum and s<=maximum and pairs.count(s) == 0):
					pairs.append(s)
					total+=1
				switches-=1
		# ###########################
		base[i] = "Case #" + str(i+1) + ": "+str(total)
	r = open("Results.txt", "w")
	for line in base:
		r.write("%s\n" % line)
	f.close()
	r.close()
	
if __name__ == "__main__":
	filename = sys.argv[1]
	numbers(filename)