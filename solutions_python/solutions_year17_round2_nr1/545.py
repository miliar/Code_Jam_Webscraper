#!/usr/bin/env python


def solve_case():
        pass



def main(argv):
        fout_name = argv[1].split(".")[0] + ".out"
        fout = open(fout_name, "w")

        fin = open(argv[1])
        nb_cases = int(fin.readline())


        for case_no in range(1, nb_cases+1):
                print case_no
                l = fin.readline().split()
                D = float(l[0])
                N = int(l[1])
                tmax = 0.
                for i in range(N):
                        m = fin.readline().split()
                        K = float(m[0])
                        S = float(m[1])
                        if float((D-K)/S) > tmax:
                                tmax = float((D-K)/S)
                #print tmin
                res =  float(D/float(tmax))
                fout.write( "Case #{}: {}\n".format(case_no, res))

        fout.close()
        fin.close()


import sys
if __name__ == "__main__":
        main(sys.argv)
