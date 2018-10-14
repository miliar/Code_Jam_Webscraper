import sys

in_file = open(sys.argv[1])
out_file = open("out.txt", 'w')

def smart(N,K):
	if K==0 or ((K+1) % 2**N) != 0:
		return False
	else:
		return True	

result = {False: "OFF", True: "ON"}	
cases = int(in_file.readline().strip())
for case in xrange(cases):
	N, K = (int(x) for x in in_file.readline().strip().split())
	out_file.write("Case #%d: %s\n" % (case+1, result[smart(N,K)]))