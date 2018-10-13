# -*- coding: utf-8 -*-

if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print "Usage: python {0} inputfile".format(sys.argv[0])
#         quit()

    ifile = open("test.in")
    ifile = open("A-small-attempt0.in.txt")
#     ifile = open("B-small-practice.in.txt")
#     ifile = open("B-large-practice.in.txt")
    ofile = open("output.txt", 'w')
    N = ifile.readline()

    for case in range(int(N)):
        rings = 0
        line = [int(x) for x in ifile.readline().rstrip().split()]
         
        r = line[0]
        t = line[1]
#         
        i = 1
#         print t
        while 1:
            t = t - (2 * r + 2 * i - 1)
#             print t
            if t < 0:
                break
            i = i + 2
            rings += 1

        print "Case #{0}: {1}".format(case + 1, rings)
        ofile.write("Case #{0}: {1}\n".format(case + 1, rings))

    ifile.close()
    ofile.close()