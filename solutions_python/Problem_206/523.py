def anny(d, n, horses):
    max_time = max(map(lambda x: float(d-x[0])/x[1], horses))
    return d/max_time

def main(fname):
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        d, n = map(int, in_fd.readline().strip().split(" "))
        horses = []
        for j in xrange(n):
            horses.append(map(int, in_fd.readline().strip().split(" ")))
        max_speed = anny(d, n, horses)
        out_fd.write("Case #%d: %f\n" % (i+1, max_speed))
    in_fd.close()
    out_fd.close()
