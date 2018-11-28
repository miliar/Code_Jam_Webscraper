import sys
assert len(sys.argv) == 2
read  = open(sys.argv[1], "r")
write = open(sys.argv[1]+".out", "w")


jam = "welcome to code jam"
jamlen = len(jam)

N = read.readline()
N = int(N)


def find(index_line, index_jam):
    global K, line, linelen
    if index_jam == jamlen:
	K += 1
	return
    j = jam[index_jam]
    index_jam += 1
    for i in range(index_line, linelen):
	if j == line[i]:
	    find(i, index_jam)

for n in range(N):
    line = read.readline().strip()
    linelen = len(line)
    K = 0
    find(0, 0)

    K = K % 1000
    write.write("Case #%s: %04i\n" % (n+1, K))
    print "Case #%s: %04i" % (n+1, K)

