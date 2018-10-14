import math

t = int(raw_input())
for i in xrange(1, t + 1):
	n= int(raw_input())
	b= len(str(n))
	def all9(k) :
		k1= len(str(k))
		if k1==1 :
			return 9
		else:
			return 9*pow(10,k1-1)+all9(int(k/10))

	def tidy(numb):
		bnew= len(str(numb))
		if bnew==1 :
			return numb
		else :	
			d1= int(numb/pow(10,bnew-1))
			d2= int(numb/pow(10,bnew-2))-(10*d1)
			if d1<d2 :
				return (d1*pow(10,bnew-1)) + tidy(numb%pow(10,bnew-1))
			elif d1==d2 :
				#print(numb%pow(10,bnew-1))
				k = tidy(numb%pow(10,bnew-1))
				if k == (numb%pow(10,bnew-1)) :
					return numb
				else :	
					return tidy((d1*pow(10,bnew-1)) + k)
			else :
				return ((d1 - 1)*pow(10,bnew-1)) + int(all9(numb)/10)








	print "Case #{}: {}".format(i, tidy(n))