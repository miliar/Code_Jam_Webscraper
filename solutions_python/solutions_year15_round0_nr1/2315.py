#input_ = ["4", "4 11111", "1 09", "5 110011", "0 1"]
import sys

def standingOvation(input_, T):
	count = T

	result = []
	for T in range(0, count):
		S_max, S = input_[T].split()
		invited = 0
		rsvp = 0
		for i in range(0, int(S_max)+1):
			invited += int(S[i])
			invite = i+1 - invited
			if invite > rsvp:
				rsvp = invite
		print "Case #%d: %s"%(T+1, rsvp)
		result.append("Case #%d: %s"%(T+1, rsvp))
	return result

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    inp = []
    for _t in xrange(t):
        line =  f.readline().strip()
        inp.append(line)

    result = standingOvation(input_=inp, T=t)
    with open("problemA_large.out", 'w') as f_:
    	for r in result:
    		f_.write(r + '\n')
