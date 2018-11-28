import string

def solveBrute(R, C, W):
    if R == 1:
        if W == 1:
            return C
        if W == 2:
            return (C+1)/2 + 1
        if W == 3:
            return (C+2)/3 + 2
        return (C+(W-1))/W + (W-1)
    if W == 1:
        return R * C


def test(inputs, ans):
	b = solveBrute(*inputs)
	if (b != ans):
		print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    test((1, 5, 2), 4)
    test((1, 6, 2), 4)
    test((1, 4, 2), 3)
    test((1, 7, 7), 7)
    test((1, 10, 7), 8)

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))    

    for k in xrange(1,T+1):
        print k
        R, C, W = map(int,string.strip(raw_input()).split())

        answer = solveBrute(R, C, W) # add appropriate arguments
        outfile.write('Case #%d: %s\n' % (k,answer))

if __name__ == '__main__':
    main()