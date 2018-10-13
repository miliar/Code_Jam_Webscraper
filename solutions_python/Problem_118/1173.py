'''
Created on Apr 13, 2013

@author: nils
'''

import sys
import fairsquare as fs

def main():
    print("Working...")
    work_files(sys.argv[1], sys.argv[2])
    print("Done.")


def work_files(fin, fout):
    with open(fin) as in_, open(fout, 'w') as out_:
        num_test = (int(in_.readline().strip()))
        for i in range(num_test):
            
            print("Working on %d" % (i + 1))
            
            r = [int(x) for x in in_.readline().strip().split()]
            sol = fs.solve(r[0], r[1])
            out_.write("Case #%d: %d\n" % (i+1, sol)) 

if __name__ == '__main__':
    main()