import sys

# read the whole file specified as an argument into memory
filename = "crop_triangles.in"
if len(sys.argv) > 1:
    filename = sys.argv[1]
lines = [line.strip() for line in open(filename)]

# process the cases
cases = int(lines[0])
offset = 1
for case in range(1, cases + 1):

    # extract the tree details
    tokens = lines[offset].split(" ")
    n = int(tokens[0])
    A = int(tokens[1])
    B = int(tokens[2])
    C = int(tokens[3])
    D = int(tokens[4])
    x0 = int(tokens[5])
    y0 = int(tokens[6])
    M = int(tokens[7])

    # generate tree co-ordinated
    X = x0
    Y = y0
    xy = [(X, Y)]
    xy_set = set()
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        xy.append((X, Y))

    # brute force
    count = 0
    for xyi1 in range(0, len(xy)):
        for xyi2 in range(1+xyi1, len(xy)):
            for xyi3 in range(1+xyi2, len(xy)):
                xc = (xy[xyi1][0] + xy[xyi2][0] + xy[xyi3][0]) / 3.0
                yc = (xy[xyi1][1] + xy[xyi2][1] + xy[xyi3][1]) / 3.0
                if (abs(int(xc) - xc) < 1e-6) and (abs(int(yc) - yc) < 1e-6):
                    count = count + 1
                    
    # output the results
    print "Case #%d: %d" % (case, count)

    offset = offset + 1

