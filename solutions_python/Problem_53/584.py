
def d2b(n):
	bStr = ''
	#if n < 0: raise ValueError, "must be a positive integer"
	if n == 0: return '0'
	while n > 0:
		bStr = str(n % 2) + bStr
		n = n >> 1
	return bStr

def input() :
	t = int( raw_input())
	for i in xrange(0,t) :
		val = raw_input()
                inp = val.split()
		n = int(inp[0])
		k = int(inp[1])
                bstr=int(d2b(k))
		#print bstr
                if k < n : 
			print "Case #%d: OFF" % (i+1)
			continue 
                val=bstr % int(d2b(2**n))
		#print val
                if val == int(d2b((2**n) - 1)) : 
                	print "Case #%d: ON" % (i+1)
                else :
                	print "Case #%d: OFF" % (i+1)

if __name__ == "__main__" :
        input()
