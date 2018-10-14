import sys

def readInt():
	return int(sys.stdin.readline().strip())

def readInts():
	return list(map(int, sys.stdin.readline().strip().split(" ")))

def readLine():
	return list(sys.stdin.readline().strip().split(" "))

TC = readInt()

for c in xrange(TC):
    line = readLine();

    C = int(line[0])
    combine = {}
    for i in xrange(C):
        three = line[1+i]
        if three[0] <= three[1]:
            combine[three[0]+three[1]] = three[2]
        else:
            combine[three[1]+three[0]] = three[2]
    #print combine

    D = int(line[C+1])
    clear = {}
    for i in xrange(D):
        pair = line[C+2+i]
        try:
            clear[pair[0]].append(pair[1])
        except:
            clear[pair[0]] = [pair[1]]
        if pair[0] != pair[1]:
            try:
                clear[pair[1]].append(pair[0])
            except:
                clear[pair[1]] = [pair[0]]
    #print clear

    N = int(line[C+D+2])
    inv = line[C+D+3]
    L = ['$']
    for i in xrange(N):
        x = inv[i]
        loop = True
        while loop:
            y = L[len(L)-1]
            if x <= y:
                key = x+y
            else:
                key = y+x
            try:
                x = combine[key]
                L.pop()
            except:
                loop = False
        try:
            for exc in clear[x]:
                if exc in L:
                    L = []
                    x = '$'
        except:
            pass
        L.append(x)
    L.pop(0)
    #print L

    print "Case #" + str(c+1) + ": [" + ", ".join(L) + "]"
