'''
usage:
    python prob_B.py <input_file>

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

    colordic={0:"R",1:"O",2:"Y",3:"G",4:"B",5:"V",6:"R",7:"O"}
    twocolor={1:4,3:0,5:2,7:4}

    with open(infile) as fin:
        line=fin.readline()
        nCases=int(line.strip())
        for i in range(0,nCases):
            line=fin.readline()
            line=line.strip()
            parts=line.split()
            n=int(parts[0])
            ans=""
            unicorns=[int(parts[1]),int(parts[2]),int(parts[3]),int(parts[4]),int(parts[5]),int(parts[6]),int(parts[1]),int(parts[2])]
            #r=int(parts[1])
            #o=int(parts[2])
            #y=int(parts[3])
            #g=int(parts[4])
            #b=int(parts[5])
            #v=int(parts[6])

            #if ((r+o+v)*2>n) or ((y+o+g)*2>n) or ((b+g+v)*2>n):
            if (sum(unicorns[5:])*2>n) or (sum(unicorns[1:4])*2>n) or (sum(unicorns[3:6])*2>n):
                fout.write("Case #"+str(i+1)+": IMPOSSIBLE\n")
                continue

            unicorns=unicorns[:6]
            max_u=max(unicorns)
            ind=unicorns.index(max_u)
            first_ind=ind
            ans=ans+colordic[ind]
            unicorns[ind]=unicorns[ind]-1
            #if ind+6<8: unicorns[ind+6]=unicorns[ind+6]-1

            for j in range(n-1):
                if ind%2==1:
                    ind=twocolor[ind]
                    ans=ans+colordic[ind]
                    unicorns[ind]=unicorns[ind]-1
                    #if ind+6<8: unicorns[ind+6]=unicorns[ind+6]-1
                elif unicorns[(ind+3)%6]>0:
                    ind=(ind+3)%6
                    ans=ans+colordic[ind]
                    unicorns[ind]=unicorns[ind]-1
                elif (first_ind not in [(ind-1)%6,ind%6,(ind+1)%6]) and (max(unicorns)==unicorns[first_ind]):
                    ind=first_ind
                    ans=ans+colordic[ind]
                    unicorns[ind]=unicorns[ind]-1
                else:
                    tmp=unicorns[:max((ind-1),0)]+unicorns[(ind+2):(ind+5)]
                    max_u=max(tmp)
                    tmp_ind=tmp.index(max_u)
                    if tmp_ind<(ind-1): ind=tmp_ind
                    elif ind<1: ind=tmp_ind+2
                    else: ind=tmp_ind+3
                    ans=ans+colordic[ind]
                    unicorns[ind]=unicorns[ind]-1
                    #if ind+6<8: unicorns[ind+6]=unicorns[ind+6]-1

            fout.write("Case #"+str(i+1)+": "+ans+"\n")                    

    fout.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())