

def a(l):
	x=0
	for i in l:
		x=x^i
	return x 

f=open("C-large.in","r")


T=int(f.readline().rstrip('\n'))
for i in range(T):
	sean=[]
	patrick=[]
	N=int(f.readline().rstrip('\n'))
	candies=f.readline().rstrip('\n').split(" ")
	candies_int=[]
	for candy in candies:
		candies_int.append(int(candy))
	flag=0
	if a(candies_int)==0:
		for candy in candies_int:
			temp_candy=candies_int[:]
			temp_candy.remove(candy)
			if a(temp_candy)==candy:
				if flag==0:
					m=candy
					flag=1
				else:
					if candy<m:
						m=candy
		candies_int.remove(m)
		result=0
		for candy in candies_int:
			result=result+candy
		print "Case #"+str(i+1)+": "+str(result)
	else:
		print "Case #"+str(i+1)+": NO"
	
	

