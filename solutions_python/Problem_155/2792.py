#!/bin/bash

import copy

def main():
    z=0
    y=0
    f = open("A-large.in", 'r')
    fp = open("output_large.txt", 'w')
    k=1
    for i in f:
        q = i.split(" ")
        print q[0], q[1]
        a = q[0]
        b = q[1]
        s = range(0, int(a)+1)
        j=0
        p = b.strip('\n')
        for i in p:
            if (int(i) == 0):
                pass
            else:
                diff = s[j] - z
                if(diff >= 0):
                    y = y + diff
                    z = z + diff+int(i)
                elif (diff < 0):
                    z = z + int(i)
            j = j+1
        xx = "Case #"+str(k)+": "+str(y)+"\n"
        k = k+1
        fp.write(xx)
        z = 0
        y= 0


if __name__ == '__main__':
    main()
