#!/usr/bin/env python


def solve_case(S):
        N = []
        for s in S:
                N.append(int(s))

        # print N
        for i in range(len(N) - 1):
                if N[i] <= N[i+1]:
                        continue
                # print "problem"
                N[i] -= 1

                for j in range(i+1, len(N)):
                        N[j] = 9

                for j in reversed(range(1, i+1)):
                        if N[j-1] > N[j]:
                                N[j-1] -= 1
                                N[j] = 9
                        else:
                                break
        return ("".join(str(x) for x in N)).lstrip('0')


def main(argv):
	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
                print "Case #", case_no
                l = fin.readline().split()
		fout.write( "Case #{}: {}\n".format(case_no, solve_case(l[0])))
	fout.close()
        fin.close()


import sys
if __name__ == "__main__":
        main(sys.argv)
