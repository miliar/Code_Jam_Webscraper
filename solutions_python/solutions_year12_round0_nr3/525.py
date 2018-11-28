import sys

def recycled_pairs(s):
	x = s.split()
	a = int(x[0])
	b = int(x[1])
	n = 0
	
	for i in range(a,b+1):
		recycles=get_recycles(i)
		for j in recycles:
			if a <= j and j < i and i <= b and len(str(i)) == len(str(j)):
				n += 1
	return n
		
def get_recycles(n):
	a = str(n)
	n = len(a)
	x = []
	for i in range(1,n):
		tmp=int(a[i:]+a[:i])
		x.append(tmp)
	return set(x)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
    lines =[line.strip() for line in open(fn)]
    lines.pop(0)
    
    for line in range(len(lines)):
		print "Case #"+str(line+1)+": "+str(recycled_pairs(lines[line]))
