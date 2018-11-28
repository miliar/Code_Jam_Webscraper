# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python {0} inputfile".format(sys.argv[0])
        quit()

    ifile = open(sys.argv[1])
    ofile = open("output.txt", 'w')
    N = ifile.readline()

    for case in range(int(N)):
        line = ifile.readline().rstrip().split()
        
        c = float(line[0])
        f = float(line[1])
        x = float(line[2])
        
        sec = 0
        add_cookie = 2
        
        while(1):
            tmp_sec = sec + x / add_cookie
            if x <= c:
                 ret = tmp_sec
                 break
            elif tmp_sec < sec + c / add_cookie + x / (add_cookie + f):
                ret = tmp_sec
                break
            else:
                sec = sec + c / add_cookie
                add_cookie = add_cookie + f

        print "Case #{0}: {1:.7f}".format(case + 1, ret)
        ofile.write("Case #{0}: {1:.7f}\n".format(case + 1, ret))

    ifile.close()
    ofile.close()
