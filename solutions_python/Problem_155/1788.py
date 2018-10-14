#from __future__ import print_function
import sys

if __name__ == "__main__":
    fi = open('test.in', 'r')
    fo = open('test.out', 'w+')

    len = fi.readline() # get rid of first line.


    for T, line in enumerate(fi):
        n = 0
        count = 0
        size, people = line.split()
        size = int(size)

        for Sn, p in enumerate(people): # Sn current shyness
            p = int(p) # current number of people of said shyness
            if Sn > n:
                count += 1
                n += 1
            n += p

        print("Case #{0}: {1}".format(T+1, count))
        fo.write("Case #{0}: {1}\n".format(T+1, count))
        #print("Case #{0}: {1} -- {2}".format(T+1, count, people))
    fo.close()