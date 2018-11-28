import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

def process(wires):
	for start in range(len(wires)):
		wi = wires[start]
		return len(filter(lambda x: x[1] < wi[1], wires[start:]))
		
	

for i in range(num):
	wnb = int(fi.readline().strip("\n").split()[0])
	wires = []
	for j in range(wnb):
		wi = fi.readline().strip("\n").split()
		wi = [int(wi[0]), int(wi[1])]
		wires += [wi]
	wires.sort()
	ret = process(wires)
	print ("Case #%i: %i") % (i+1, ret)
