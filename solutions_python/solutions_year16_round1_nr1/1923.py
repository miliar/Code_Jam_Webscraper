import sys

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())

    for i in xrange(t):
	s = f.readline().strip()

	res = ""
	for c in s:
	    if res+c > c+res:
		res = res+c
	    else:
		res = c+res
		
	print "Case #"+str(i+1)+": "+res
    f.close()

if __name__ == "__main__":
    main()
