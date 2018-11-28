
def main(line):
    dad=map(int,line.split(" "))
    ng=dad[0]
    s=dad[1]
    p=dad[2]
    #print "ng ",ng," s:",s," p:",p
    resp=0
    for i in xrange(ng):
        v=dad[i+3]
        #print v
        if v>=3*p-2:
            resp+=1
        elif v>=3*p-4 and s>0 and v>=p:
            s-=1
            resp+=1
    return resp


if __name__ == '__main__':
	import sys
        #print sys.stdin.readline()
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip())
		print "Case #%d: %s" % (i + 1, res)	
