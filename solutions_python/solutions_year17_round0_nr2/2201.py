t = int(raw_input())  # read a line with a single integer

def round_down(num, divisor):
    return num - (num%divisor)
	
for i in xrange(1, t + 1):
  N = int(raw_input())
  r=N
  pow=1
  while N > 0: 	
	if str(N)=="".join(sorted(str(N))): r=N; break
	
	divisor = 10**(pow-1)
	if N > divisor: N=round_down(N,divisor)
	N = N-1
	pow=pow+1
  print "Case #{}: {}".format(i, r)	