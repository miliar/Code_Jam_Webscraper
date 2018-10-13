#!/usr/bin/python

#GOOGLE CODE JAM #########
#name: Snapper Chain #####
#by: jm ###### 8/5/10 ####
##########################

def estat(t,n,k):
	resultat=''
	estat=0
	accions=k
	for i in range(n):
		if(accions&0x01):
			estat=1
			accions=k>>(i+1)
		else:
			estat=0
			break
	if(estat):
		resultat="ON"
	else:
		resultat="OFF"
	print "Case #"+str(t)+": "+resultat

if __name__ == '__main__':
	from sys import argv
	from string import split
	
	fitxer=argv[1]
	f=open(fitxer,'r')
	t=int(f.readline())
	x=0
	while(x<t):
		x=x+1
		n_k=f.readline()
		n=int(split(n_k)[0])
		k=int(split(n_k)[1])
		estat(x,n,k)
	f.close()