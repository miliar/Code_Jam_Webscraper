import math

def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)

def main():
	num = input()
	for i in range(num):
		str = raw_input()
		str = str.split()
		if(len(str)==4):
			x = int(str[1])
			y = int(str[2])
			z = int(str[3])

			d1 = abs(x-y)
			d2 = abs(x-z)
			d3 = abs(y-z)
			best = gcd(d1,gcd(d2,d3))

			x1 = x % best
			y1 = y % best
			z1 = z % best

			ans = 0
			while((x1 != 0) and (y1 != 0) and (z1 != 0)):
				add = best - x1
				if((best - y1) < add):
					add = best - y1
				if((best - z1) < add):
					add = best - z1
				ans += add
				x1 = (x1 + add) % best
				y1 = (y1 + add) % best
				z1 = (z1 + add) % best

			data = "Case #%d: %d" % (i+1,ans)
			print data
#			print "T: ", best
#			print (x+ans)/best
#			print (y+ans)/best
#			print (z+ans)/best
		if(len(str)==3):
			x = int(str[1])
			y = int(str[2])

			d1 = abs(x-y)
			best = d1

			x1 = x % best
			y1 = y % best

			ans = 0
			while((x1 != 0) and (y1 != 0)):
				add = best - x1
				if((best - y1) < add):
					add = best - y1
				ans += add
				x1 = (x1 + add) % best
				y1 = (y1 + add) % best


			data = "Case #%d: %d" % (i+1,ans)
			print data
#			print "T: ", best
#			print (x+ans)/best
#			print (y+ans)/best
		
main()
