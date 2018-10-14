import sys
import os

fs = []

def invert_str(s) :
	inv = ""
	for c in s :
		inv = c + inv

	return inv

def is_pal(n) :
	l = len(n)/2
	return invert_str(n[:l]) == n[-l:]

def bt(s, one) :
	if len(s) > 26 or one > 5:
		return
		
	inv = invert_str(s)

	pal = int(s+inv)
	pal2 = pal*pal;
	if is_pal(str(pal2)) :
#		print pal
		fs.append(pal)

	for i in "012":
		pal = int(s+i+inv)
		pal2 = pal*pal;
		if is_pal(str(pal2)) :
#			print pal
			fs.append(pal)

	for i in "01":
		bt(s+i, one+(i=="1"))
	
	return


def BS(A) :

	left = -1; right = len(fs)
	while left < right-1 :
		mid = (left + right) / 2
		if(fs[mid]*fs[mid] < A) : left = mid
		else : right = mid
	return right

def BS_(A) :

	left = -1; right = len(fs)
	while left < right-1 :
		mid = (left + right) / 2
		if(fs[mid]*fs[mid] <= A) : left = mid
		else : right = mid
	return right


if __name__ == "__main__" :

	fs.append(1);fs.append(2);fs.append(3)
	for i in range(0, 50) :
		fs.append( int("2"+ "0"*i + "2") )
#		print ("2"+ "0"*i + "2")
		if i % 2 != 0 :
			fs.append(int ( "2"+ "0"*(i/2) + "1" + "0"*(i/2) + "2" ))
#			print ( "2"+ "0"*(i/2) + "1" + "0"*(i/2) + "2" )
	bt("1", 1)

	fs.sort()
#	for i in fs :
#		print i
#	print len(fs)

	casos = int(sys.stdin.readline())
	for t in range(1, casos+1) :
		line = sys.stdin.readline()
		val = line.strip()
		A = int(val.split()[0])
		B = int(val.split()[1])

		p1 = BS(A)
		p2 = BS_(B)
		ret = max(0, p2 - p1);
		print "Case #" + str(t) + ": %d" % ret

