'''
usage:
    python prob_A.py <input_file>

output: file with the name "<input_file>.out"
'''


import sys
import os

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
            k=int(parts[1])
            tmp=parts[0].replace("-","0")
            num_str=tmp.replace("+","1")
            num=int(num_str,2)

            all_flips=[]
            flips=[]
            max_flips=len(num_str)-k+1
            target=pow(2,len(num_str))-1
            rem=target-num

            if num==target:
                fout.write("Case #"+str(i+1)+": 0\n")
                continue

            s_flip=pow(2,k)-1

            while s_flip<=target:
                flips.append(s_flip)
                s_flip=s_flip*2

            flips=list(set(flips))
            all_flips.append(flips)

            tmp=[]
            for j in range(max_flips-1):
                tmp=[]
                for x1 in all_flips[j]:
                    for x2 in flips:
                        tmp.append(x1^x2)
                tmp=list(set(tmp))
                all_flips.append(tmp)

            ans=-1
            for j in range(max_flips):
                if rem in all_flips[j]:
                    ans=j+1
                    break

            if ans==-1: fout.write("Case #"+str(i+1)+": IMPOSSIBLE\n")
            else: fout.write("Case #"+str(i+1)+": "+str(ans)+"\n")

    fout.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())