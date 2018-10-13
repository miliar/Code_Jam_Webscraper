#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     08/05/2011
# Copyright:   (c) wani 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

def getsize(R,C,plate):
    if R > C :
        max = C
    else:
        max = R
    sizes = range(3,max+1)
    sizes.reverse()
    for size in sizes:
        xx = C - size +1
        yy = R - size +1
        for x in range(xx):
            for y in range(yy):
                center = [x+(size-1)/2.0,y+(size-1)/2.0]
                cw = [0,0]
                for i in range(size):
                    for j in range(size):
                        if [i,j] == [0,0] or [i,j] == [0,(size-1)] or [i,j] == [(size-1),0] or [i,j] == [(size-1),(size-1)]:
                            continue
                        a = x + i
                        b = y + j
                        w =  plate[b][a] #y,x
                        cw = [cw[0] + w*(i-(size-1)/2.0),cw[1] + w*(j-(size-1)/2.0)]
#                print size,cw,center,(x,y)
                if cw == [0,0]:
                    return size
    return 0

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        R,C,D = [ int (x) for x in f.readline().strip().split()]
        plate = []
        for n in range(R):
            ds = []
            for x in f.readline().strip():
                x = int(x)# + D
                ds.append(x)
            plate.append(ds)
        size = getsize(R,C,plate)
        if size < 3:
            out = "Case #%d: %s"%(i+1,"IMPOSSIBLE") + "\n"
        else:
            out = "Case #%d: %d"%(i+1,size) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()
