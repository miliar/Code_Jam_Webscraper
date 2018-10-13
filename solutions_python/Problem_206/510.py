import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input

cases=int(input().strip())
for cs in range(1,cases+1):
	d,h=map(int,input().strip().split())
	mt=0
	for i in range(h):
		k,s=map(int,input().strip().split())
		mt=max(mt,float(d-k)/s)
	mt=0.0 if mt<=0 else d/mt
	print("Case #"+str(cs)+": {0:0.6f}".format(mt))
