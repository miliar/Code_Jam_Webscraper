import sys

def convTidy(n):
    if len(str(n)) == 1:
	return n

    ind = len(str(n))-2
    ar = [int(elem) for elem in str(n)]
    f = False

    while ind >= 0:
	if ar[ind] > ar[ind+1]:
	    ar[ind+1] = 9
	    ar[ind] -= 1
	    
	    if ind+2 < len(ar):
	        for ii in xrange(ind+2, len(ar)):
		    ar[ii] = 9	    

	ind -= 1
     
    ind = 0
    while ind < len(ar):
	if ar[ind] == 0:
	    ind += 1
	else:
	    break

    res = ""
    while ind < len(ar):
	res += str(ar[ind])
        ind += 1

    return res


def main():
    f = open(sys.argv[1])

    t = int(f.readline().strip())
    for i in xrange(t):
	num = int(f.readline().strip())
	num = convTidy(num)
	print "Case #"+str(i+1)+": "+str(num)

    f.close()

if __name__ == "__main__":
    main()
