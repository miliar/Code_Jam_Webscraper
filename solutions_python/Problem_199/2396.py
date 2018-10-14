#!/usr/bin/env python


def flip(pkin, start, length):
#        print "flip"
        pkout = pkin[:start]
        for i in range(length):
                if pkin[start+i] == '-':
                        pkout += '+'
                else:
                        pkout += '-'
        pkout += pkin[start+length:]
        return pkout

        
def solve_case(pks, K):
#        print pks, K
        cur_pks = pks
        nb_flip = 0
        for i in range(len(pks)):
#                print cur_pks
                if cur_pks[i] == '+':
                        continue

#                print (len(pks) - i), "<", K
                
                if (len(pks) - i) < K:
#                        print "I"
                        return "IMPOSSIBLE"
                cur_pks = flip(cur_pks, i, K)
                nb_flip += 1
        return nb_flip




def main(argv):
	fout_name = argv[1].split(".")[0] + ".out"
	fout = open(fout_name, "w")

	fin = open(argv[1])
	nb_cases = int(fin.readline())


	for case_no in range(1, nb_cases+1):
                print case_no
                l = fin.readline().split()
		fout.write( "Case #{}: {}\n".format(case_no, solve_case(l[0], int(l[1]))))

	fout.close()
        fin.close()


import sys
if __name__ == "__main__":
        main(sys.argv)
