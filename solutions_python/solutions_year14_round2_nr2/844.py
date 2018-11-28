import numpy as np
import fileinput

def main():
    input = []
    for line in fileinput.input():
        input.append(line)

    numcases = int(input[0])

    for i in xrange(numcases):
        info = input[i+1]
        a,b,k = [int(num) for num in info.split()]
        #tickets = range(k)
        count = 0
        v1,v2 = np.arange(a,dtype=int), np.arange(b,dtype=int)
        out_arr = np.zeros((a,b),dtype=int)
        for j in xrange(a):
            out_arr[j] = v1[j] & v2
        #print out_arr
        count = sum(sum(out_arr < k))
        print "Case #" + str(i + 1) + ":",
        print count


if __name__ == '__main__':
    main()
