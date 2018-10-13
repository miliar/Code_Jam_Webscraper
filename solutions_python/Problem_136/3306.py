import sys, string

def cookies(c, f, x):
#    print "running case %f, %f, %f" % (c, f, x)
    rcur = 2.0
    t = 0.0
    while 1:
        rnext = rcur + f
        dtfact = c / rcur + x / rnext
        dtx = x / rcur
#        print "round t %f, rcur %f, w/o factory %f, with factory %f" % (t, rcur, dtx, dtfact)
        if dtfact >= dtx:
            t += dtx
            break
        t += c / rcur
        rcur = rnext
    return t

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        line = line.rstrip()
        c, fc, x = map(float, line.split(" "))
#        print "running case %d, %f, %f, %f" % (i+1, c, f, x)
        ans = cookies(c, fc, x)
        sys.stdout.write("Case #%d: %0.7f\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)