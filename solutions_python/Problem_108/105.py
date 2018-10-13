
import sys

T = int(sys.stdin.readline())



for t in range(1, T+1):
		N = int(sys.stdin.readline())
		v = list()
		for i in range(N):
				a = sys.stdin.readline().split()
				a = map(int, a)
				v.append((a[0], a[1]))
		D = int(sys.stdin.readline())
		
		#print v
		def solve(at, atidx, rt):
				rch = 2*(rt-at)
				#print at, atidx, rt, rch
				if at+rch >= D:
						return True
				else:
						dr = 0
						if rch > 0: dr = 1
						else: dr = -1
						idx = atidx+dr
						while 0<=idx and idx<len(v) \
									and abs(at-v[idx][0]) <= abs(rch) \
									and v[idx][0]!=rt:
								#and v[idx][1]>=abs(v[idx][0]-rt):
								#print "I", idx
								newrt = v[idx][0]
								vlen = v[idx][1]
								newat = newrt - (rt-newrt)/(rt-newrt)*min(vlen, abs(rt-newrt))
								if solve(newat, idx, v[idx][0]):
										#print rt
										return True
								#print "false"

								idx += dr

				#print "Ret false"
				return False

		if solve(0, 0, v[0][0]):
				print "Case #%d: YES" % t
		else:
				print "Case #%d: NO" % t
		



