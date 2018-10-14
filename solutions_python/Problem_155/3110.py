import sys;

#nocases
infile = open(sys.argv[1]);
outfile = open(sys.argv[2], "w");
n = int(infile.readline());
for j in xrange(n):
    if (j>0):
        outfile.write("\n");
    k, si = infile.readline().split();
    k = int(k);
    totalsofar=0; fr=0; minreq = 0;
    for c in si:
        newpeeps = int(c);
        if (minreq <= totalsofar):
            totalsofar += newpeeps;
        else:
            newfr = (minreq-totalsofar);
            totalsofar += (newpeeps+newfr);
            fr += newfr
        minreq += 1;
    outfile.write("Case #%d: %d" % (j+1, fr))
outfile.close();
infile.close();