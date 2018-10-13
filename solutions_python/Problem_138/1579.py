#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nishant
#
# Created:     13-04-2014
# Copyright:   (c) Nishant 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    input_file  = "D-large.in"
    output_file = "D-large.out"
    f = open(input_file, 'r')
    o = open(output_file, 'w')

    cases = int(f.readline())

    for i in range(1, cases + 1):
        N = int(f.readline())
        arr1 = f.readline().split()
        arr2 = f.readline().split()

        a1 = [float(a) for a in arr1]
        a1.sort()
        a2 = [float(a) for a in arr2]
        a2.sort()

        # Deceitful War
        j = 0 # counter of 2nd
        for l in range(0, N):
            if a1[l] > a2[j]:
                j += 1

        # War
        k = 0
        for l in range(0, N):
            if a2[l] > a1[k]:
                k += 1
        o.write("Case #%s: %s %s\n" %(i, j, N - k))

    f.close()
    o.close()



if __name__ == '__main__':
    main()