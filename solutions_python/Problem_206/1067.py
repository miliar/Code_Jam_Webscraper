from __future__ import division

def problem():
	inp = raw_input()
	K, H = inp.split(' ')
	K = int(K)
	H = int(H)
	km_h = []
	spd_h = []
	for x in range(H):
		inp = raw_input()
		k, s = inp.split(' ')
		k = int( k )
		s = int( s )
		km_h.append(k)
		spd_h.append(s)
	return calculate( K, H, km_h, spd_h )

def calculate( K, H, km, spd ):
	max_time = 0
	for ind in range(len(km)):
		dis = K - km[ind]
		time = dis / spd[ind]
		max_time = max(max_time, time)

	return K / max_time
 
if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while ( T > 0 ):
		print "Case #%s: %.6f" % ( case, problem() )
		case = case + 1
		T = T - 1
 