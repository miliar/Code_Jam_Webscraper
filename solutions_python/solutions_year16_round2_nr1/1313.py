#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saurabh
#
# Created:     30/04/2016
# Copyright:   (c) Saurabh 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    fo = open("A-large.in","r")
    fp = open("output2.txt", "w")
    test = int(fo.readline())
    tri = 1
    while test > 0:
        test -= 1
        sst = fo.readline()

        ls = ["ZERO", "TWO","FOUR", "ONE",  "EIGHT","THREE", "SIX","SEVEN","FIVE", "NINE"]
        ls2 = [0,2,4,1,8,3,6,7,5,9]
        k = 0
        s = ""
        while k < len(ls):
            i = ls[k]
            count = 0
            for j in i:
                if j in sst:
                    count += 1

            if count == len(i):
                for j in i:
                    if j in sst:
                        ind = sst.index(j)
                        sst = sst[0:ind] + sst[ind+1: len(sst)]
                s += str(ls2[k])
            else:
                k += 1


        fp.write("Case #"+str(tri)+": "+''.join(sorted(s)))
        tri+=1
        fp.write("\n")

if __name__ == '__main__':
    main()

