import sys

def process(inp):
	data = inp.readline().strip().split()
	destination = int(data[0])
	num_horses = int(data[1])

	horses = []
	for i in range(num_horses):
		data = inp.readline().strip().split()
		pos = int(data[0])
		speed = int(data[1])
		horses.append( (pos, speed ) )

	horses.sort( key=lambda h:h[0] )
	when_will_arrive = 0
	for h in horses:
		pos, speed = h
		when_will_arrive = max( when_will_arrive, (destination-pos) / float(speed) )

	speed = destination / when_will_arrive
	return speed


inp = open(sys.argv[1],"r")
count = int(inp.readline())
for i in range(count):
	outp = process(inp)
	print "Case #%i: %0.6f"%( i+1, outp )
