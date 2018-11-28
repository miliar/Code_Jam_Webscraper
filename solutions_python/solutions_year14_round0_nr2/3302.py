__author__ = 'jesse.vera'

if __name__ == "__main__":
    f_in = open("B-large.in", "rw+")
    f_out = open("B-large.out", "w")
    num = f_in.readline().strip()

    for i in xrange(int(num)):
        c, f, x = [float(num) for num in f_in.readline().strip().split(' ')]

        rate = 2
        eta = x / rate
        time = 0
        while True:
            nextfarm = c / rate
            nexteta = x / (rate + f)
            if nexteta + nextfarm < eta:
                rate = rate + f
                time = time + nextfarm
                eta = nexteta
            else:
                break

        f_out.write("Case #%s: %s\n" % (i+1, time + eta))