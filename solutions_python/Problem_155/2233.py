from __future__ import division
import math




if __name__ == "__main__":
    ifile = open("A-large.in","r")
    ofile = open("A-large.out","w")
    data = ifile.readlines()
    ifile.close()
    cases = int(data.pop(0))
    case = 1
    for line in data:
        sect = line.split(" ")
        Smax = int(sect[0])
        count = 0
        additions = 0
        for i in range(Smax+1):
            current = int(sect[1][i])
            if i > count:
                additions += (i-count)
                count += current + (i-count)
            else:
                count += current
        output =  "Case #"+str(case)+": "+str(additions)
        ofile.write(output+"\n")
        print output
        case += 1
    ofile.close()
            
