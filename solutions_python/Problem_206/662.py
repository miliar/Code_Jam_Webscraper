def cruise(d, n, horses):
	time = 0.0
	for horse in horses:
		position = horse[0]
		speed = horse[1]
		time = max(time, float(d-position)/speed)

	return d / time

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        d, n = (int(n) for n in raw_input().strip().split())
        horses = list()
        for i in range(n):
        	horses.append(list(int(n) for n in raw_input().strip().split()))
    	horses.sort()
        print "Case #%d: %f" % (T+1, cruise(d, n, horses))