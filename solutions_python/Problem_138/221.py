import sys, copy;
file = open("newfile.txt", "w")

file.write("hello world in the new file\n")

file.write("and another line\n")

file.close()

ad = 0
af = 0
def solve(a, b, c, d):
    global ad, af;
    a.sort(reverse=True)
    b.sort(reverse=True)

    if ( a[n - 1] > b[0] ) :
        ad = n;
        af = n;
        return;
    if ( a[0] < b[n - 1] ) :
        ad = 0;
        af = 0;
        return;
    c = copy.deepcopy(a);
    d = copy.deepcopy(b);
    m = n;
    af = 0;
    for i in range(n) :
        if ( a[i] > d[0] ) :
            af = af + 1
            m = m - 1;
        else :
            for j in range(m - 1, -1, -1):
                if ( d[j] > a[i] ) :
                    m = m - 1;
                    for k in range(j, m):
                        d[k] = d[k + 1];
                    break;
    ad = 0;
    m = n;
    for i in range(n - 1, -1, -1):
        m = m - 1;
        if ( a[i] > b[i] ) :
            ad = ad + 1
        else:
            if ( a[i] < b[0] ) :
                for k in range(m):
                    b[k] = b[k + 1];
    print ad, af

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print inputFile, outputFile
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print t
    for i in range(1, t + 1):
        print "a"
        file.write("Case #" + str(i) + ": ")
        n = int(f.readline())
        a = [0 for x in xrange(n)]
        b = [0 for x in xrange(n)]
        c = [0 for x in xrange(n)]
        d = [0 for x in xrange(n)]
        a = map(float, f.readline().split())
        b = map(float, f.readline().split())

        solve(a, b, c, d);
        file.write(str(ad) + " " + str(af) + "\n")
file.close()            








