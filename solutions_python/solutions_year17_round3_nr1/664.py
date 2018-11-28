'''
usage:
    python prob_A.py <input_file>

output: file with the name "<input_file>.out"
'''


import sys
import os
import math
import itertools

def main(argv=None):
    if len(sys.argv) != 2:
        print __doc__
        sys.exit(1)

    infile=sys.argv[1]
    outfile=infile+".out_tmp"

    fout=open(outfile,"w")

    with open(infile) as fin:
        line=fin.readline()
        nCases=int(line.strip())
        for i in range(0,nCases):
            line=fin.readline()
            line=line.strip()
            parts=line.split()
            n=int(parts[0])
            k=int(parts[1])

            radi=[]
            hei=[]

            for j in range(n):
                line=fin.readline()
                line=line.strip()
                parts2=line.split()
                radi.append(float(parts2[0]))
                hei.append(float(parts2[1]))

            max_area=0
            for combs in itertools.combinations(range(n),k):
                area=0
                r_max=0
                for j in range(k):
                    area=area+hei[combs[j]]*radi[combs[j]]*2
                    if r_max < radi[combs[j]]: r_max=radi[combs[j]]
                area=area+r_max*r_max
                if area > max_area: max_area=area

            fout.write("Case #"+str(i+1)+": %.9f\n" % (max_area*math.pi))

    fout.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())