import numpy

def solve_D(infile, outfile):
    inputs = open(infile).readlines()[2::2]
    R = []
    for i, inp in enumerate(inputs):
        vals = numpy.array(map(int, inp.split()))
        res = (vals != numpy.arange(1, len(vals) + 1)).sum()
        R.append("Case #%d: %f" % (i + 1, res))
    open(outfile, "w").write("\n".join(R))
