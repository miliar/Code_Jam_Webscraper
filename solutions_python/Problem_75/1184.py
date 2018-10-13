#!usr/bin/python

def convertToTuple(a):
	b = []
	for i in range(0,len(a)):
		b.append(a[i])
	return b
		

def main():
	n = int(raw_input())
	for i in range(0,n):
		inputi = raw_input() #input raw
		arr = inputi.split()
		c = int(arr[0])
		del arr[0]
		co = dict()
		for j in range(0,c):
			s = arr[0]
			co[s[0] + s[1]] = s[2]
			co[s[1] + s[0]] = s[2]
			del arr[0]
		op = []
		o = int(arr[0]) 
		del arr[0]
		for j in range(0,o):
			s = arr[0]
			op.append(s)
			op.append(s[1] + s[0])
			del arr[0]
		length = int(arr[0])
		ma = arr[1]
		mag = convertToTuple(ma)
		magout = []
		while(mag != []):
			magout.append(mag[0])
			if(len(magout) > 1):
				if(magout[len(magout)-1] + magout[len(magout)-2] in co):
					magout[len(magout)-2] = co[magout[len(magout)-1] + magout[len(magout)-2]]
					del magout[len(magout)-1]
				else:
					for m in range(0,len(magout)-1):
						if(magout[m] + magout[len(magout)-1] in op):
							for z in range(0,len(magout)):
								del magout[0]
							break		
								  	
			del mag[0]
		strans = 'Case #{p}: {ans}'.format(p=i+1,ans=magout)
		print strans.replace("'","")
			

main()
