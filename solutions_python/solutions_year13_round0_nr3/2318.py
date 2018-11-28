from math import *

def P(n):
    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a * 10
        m = m / 10

    if( n == a):
	    return True

def test(ip):
        li = (ip.pop(0)).split()
        c = 0
        #print li
        lower_bound = int(li[0])
        upper_bound = int(li[1])
        for num in range(lower_bound, upper_bound+1):
		if P(num):
			sq_rt = sqrt(num)
			if sq_rt % 1 == .0:
				sq_rt = int(sq_rt)
				if P(sq_rt):
					 c = c + 1
        return c

def read_ip():
	f = open("/home/neo/code_jam_2013/input", "r")
	li = f.readlines()
	f.close()
	for e in range(0,len(li)):
		li[e] = li[e].strip("\n")
	#print li
	return li

def main():
	ip = read_ip()
	cases = int(ip.pop(0))
	for e in range(0,cases):
		result = test(ip)
		print "Case #" + str(e+1) + ": " + str(result)


if __name__=="__main__":
	main()
