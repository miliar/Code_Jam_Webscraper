import sys
import time


if __name__ == "__main__":

    t1 = time.clock()

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        line = f.readline()
        vals = line.strip().split()
        c = int(vals[0])
        d = int(vals[1])

        vendors = []
        for i in range(0, c):
            line = f.readline()
            vals = line.strip().split()
            p = int(vals[0])
            v = int(vals[1])
            for j in range(0, v):
                vendors.append(p)

        

        max_value = 0.0
        for i in range(0, len(vendors)):
            curr_vendor_count = 0
            for j in range(i+1, len(vendors)):
                curr_length = vendors[j] - vendors[i]
                curr_vendor_count = j-i+1
                if (curr_vendor_count-1)*d - curr_length > max_value:
                    max_value = (curr_vendor_count-1)*d - curr_length

        print "Case #%i: %f" % (testindex+1, max_value/2.0)

    t2 = time.clock()
    sys.stderr.write("runtime: %s\n" % repr(t2-t1))
