from math import sqrt, ceil, floor

def palindrom(n):
	sn = `n`
	for j in range(0, len(sn)/2):
		if sn[j] != sn[len(sn)-1-j]:
			return False
	return True

for i in range(0, input()):
	s, e = map(int, raw_input().split())
	cnt = 0
	for z in range(int(ceil(sqrt(s))), int(floor(sqrt(e)))+1):
		if palindrom(z) and palindrom(z*z):
			cnt += 1
	print 'Case #'+`i+1`+': '+`cnt`