'''
usage:
    python prob_C2.py <input_file>

output: file with the name "<input_file>.out"
'''


import sys
import os
import math

def main(argv=None):
    if len(sys.argv) != 2:
        print __doc__
        sys.exit(1)

    infile=sys.argv[1]
    outfile=infile+".out"

    fout=open(outfile,"w")

    with open(infile) as fin:
        line=fin.readline()
        nCases=int(line.strip())
        for i in range(0,nCases):
            line=fin.readline()
            line=line.strip()
            parts=line.split()
            N=int(parts[0])
            K=int(parts[1])

            lst=int(math.log(K,2))
            denom=pow(2,lst)
            quo=int((N-denom)/denom)
            rem=(N-denom)%denom

            if K>(denom+rem): part=quo
            else: part=quo+1

            if part%2==0: ans=[part/2-1,part/2]
            else: ans=[(part-1)/2,(part-1)/2]

            fout.write("Case #"+str(i+1)+": "+str(max(ans))+" "+str(min(ans))+"\n")

    fout.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())