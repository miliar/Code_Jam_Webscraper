T = int(raw_input())

def doprob():
	N, P = map(int, raw_input().split())
	G = map(int, raw_input().split())
	H = [x%P for x in G]
	H.sort()
	if P == 2:
		return H.count(0) + (H.count(1)+1)/2
	if P == 3:
		x = min(H.count(1), H.count(2))
		return H.count(0) + x + (H.count(1)+H.count(2)-2*x+2)/3
	if P == 4:
		x1 = min(H.count(1), H.count(3))
		y2 = H.count(2)%2
		y1 = H.count(1) - x1
		y3 = H.count(3) - x1
		yt = y1+y3
		out = H.count(0) + x + H.count(2)/2
		if y2 == 1:
			if yt >= 2:
				out += 1 + (yt-2+3)/4
			else:
				yt += 1
		else:
			out += (yt+3)/4
		return out

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())