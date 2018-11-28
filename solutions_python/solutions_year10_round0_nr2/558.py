import sys;
C = -2

def gcd(a,b):
	while b:
		a,b = b,a % b
	return a

cn = 0
for lin in sys.stdin:
	if C == -2:
		C = int(lin)
		continue
	if C == 0:
		break
	C -= 1
	cn += 1
	arr = lin.split(" ")
	arr = [long(el) for el in arr[1:]]
	diffs = set([abs(i-j) for i in arr for j in arr if i != j])
	diffs = [i for i in diffs]
	ans = diffs[0]
	#print ",".join([str(i) for i in diffs])

	for i in diffs:
		ans = gcd(ans,i)
	#print ans
	myans = (ans-arr[0]) % ans
	myans += ans
	myans %= ans
	print "Case #%d: %d" % (cn,myans)






