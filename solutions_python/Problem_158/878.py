import math

T = int(raw_input())


def test(X, W, H):	
	if X < 7 and (W * H) % X == 0 and (X <= W or X <= H) and (W * H != 8 if X == 4 else True):
		def cond(a, b):
			xa = min(a + 1, X)
			xb = X / xa + (X % xa)
			# print xa, xb
			return xa <= a and xb <= b or xa <= b and xb <= a

		if cond(W, H) and cond(H, W):
	
			return True
	return False


for t in xrange(T):
	X, W, H = map(int, raw_input().split())
	print "Case #%d: %s" %(t+1, "GABRIEL" if test(X, W, H) else "RICHARD")


# for h in xrange(1,5):
# 	for w in xrange(h,5):
# 		s = ""
# 		for x in xrange(1,5):
# 			R = test(x, w, h)
# 			s +="#" if R else "O"
# 			# print "%d  %d %d" %(x, w, h)
# 		print s, w, h
# 	print "--"