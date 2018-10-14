from fractions import Fraction

def safe_append(key, length, d):
    if key in d:
	d[key] += length
    else:
	d[key] = length

def parse_param():
    X, S, R, t, N =  map(int, raw_input().split())
    walkway = {}
    for i in xrange(N):
	B, E, w = map(int, raw_input().split())
	length = E - B
	X -= length
	w += S
	safe_append(w, length, walkway)
    if X > 0:
	safe_append(S, X, walkway)
    return R - S, t, walkway

def solve(R, t, walkway):
    key = walkway.keys()
    key.sort()
    canrun_t = Fraction(t, 1)
    walkway2 = {}
    for speed in key:
	lenght = walkway[speed]
	canrun = (speed + R) * canrun_t
	if canrun < lenght:
	    walkway[speed] -= canrun
	    safe_append(speed + R, canrun, walkway2)
	    break
	else:
	    del walkway[speed]
	    safe_append(speed + R, lenght, walkway2)
	    canrun_t -= Fraction(lenght, speed + R)
    time = Fraction(0, 1)
    for speed in walkway:
	length = walkway[speed]
	time += Fraction(length, speed)
    for speed in walkway2:
	length = walkway2[speed]
	time += Fraction(length, speed)
    return float(time)

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	R, t, walkway = parse_param()
	print solve(R, t, walkway)

main()

