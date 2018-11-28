'''
usage:
    python prob_B.py <input_file>

output: file with the name "<input_file>.out"
'''


import sys
import os
import re

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
            num=line.strip()
            if int(num)<10:
                fout.write("Case #"+str(i+1)+": "+num+"\n")
                continue
            first_digit=int(num[0])
            last_digit=9
            ans=""
            compens=0
            for j in range(len(num)-1,0,-1):
                curr_digit=int(num[j])-compens
                if curr_digit>=first_digit:
                    if curr_digit<=last_digit:
                        ans=str(curr_digit)+ans
                        last_digit=curr_digit
                        compens=0
                        continue
                    else:
                        ans=re.sub(r'\d','9',ans)
                        ans=str(curr_digit-1)+ans
                        last_digit=curr_digit-1
                        compens=0
                        continue
                else:
                    compens=1
                    ans="9"+re.sub(r'\d','9',ans)
                    last_digit=9
                    continue

            ans=str(int(num[0])-compens)+ans
            ind=0
            while ans[ind]=="0":
                ind=ind+1
            if ind>0: ans=ans[ind:]
            if ans=="": ans="0"
            fout.write("Case #"+str(i+1)+": "+ans+"\n")

    fout.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())