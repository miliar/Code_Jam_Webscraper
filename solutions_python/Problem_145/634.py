import sys
import numpy
import math

#data in multiple rows and one of the input columns tells which row
# def readData(f):
	# data = []
	# inputs = int(f.readline().rstrip('\n\t\r'))
	# count = 1
	# rec = []
	# temp1 = []
	# temp2 = []
	# cnt = 0
	# for line in f:
		# #print line
		# if count == 1:
			# temp = line.rstrip('\n\r\t').split()
			# for v in temp:
				# temp1.append(int(v))
			# count = 2
			# #print temp1
			# continue
		# if count == 2:
			# cnt = cnt + 1
			# temp = line.rstrip('\n\r\t')
			# temp2.append(int(temp))
			# if cnt == temp1[1]:
				# count = 1
				# cnt = 0
				# data.append([temp1, temp2])
				# temp1 = []
				# temp2 = []
	# return data	
	
#data in a single line
def readData(f):
	data = []
	inputs = int(f.readline().rstrip('\n\t\r'))
	for line in f:
		rec = []
		temp = line.rstrip('\n\r\t').split('/')
		for v in temp:
			rec.append(int(v))
		data.append(rec)
	return data	


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a
	
def main():
	"""main function
	./template1.py filename"""
	if len(sys.argv)!= 2:
		print 'usage: %run template1.py filename'
		sys.exit(1)
	f = open(sys.argv[1], 'r')
	data = readData(f)	
	f.close()
	f = open('template1.txt','w')
	count = 1
	for rec in data:
		g = gcd(rec[0],rec[1])
		rec[0]/=g
		rec[1]/=g
		l = int(math.log(rec[1],2))
		if rec[1]!=pow(2,l):
			out = 'impossible'
		else:
			cnt = 0
			while rec[0]<rec[1]:
				cnt = cnt + 1
				rec[1] = rec[1]/2
			out = str(cnt)
		print 'Case #'+str(count)+': '+out
		print >>f, 'Case #'+str(count)+': '+out
		count = count + 1
	f.close()
	
	
	
	

#to call the main function
if __name__=='__main__':
	main()