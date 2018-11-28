

f = open("A-small-attempt0.in","r")
wf = open("A-small-attempt0.out","w")


def main():
	T = int(f.readline())
	for case in range(1,T+1):
		start(case)
	f.close
	wf.close

def start(case):
	r, bp = [ int(n) for n in f.readline().split()]
	ring = 0
	while (bp > 0):
		bp = bp - (2*r+1)
		r += 2
		if(bp >= 0):
			ring += 1
	wf.write("Case #{}: {}\n".format(case,ring))




main()	