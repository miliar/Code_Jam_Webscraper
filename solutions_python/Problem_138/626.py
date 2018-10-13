# Deceitful War
# https://code.google.com/codejam/contest/2974486/dashboard#s=p3
# Qual Round 2014 D, Pts 11

import sys
import math

# Find the largest number in sorted array arr that is smaller than num
def find_closest(num, arr):
    n = len(arr)
    if n == 0:
        return(-1)
    if n == 1:
        if num > arr[0]:
            return(0)
        else:
            return(-1)
    q = n-1
    p = 0
    while p <= q:
        mid = math.floor((p+q)/2)
        if num < arr[mid]:
            q = mid - 1
        else:
            if mid+1 < n and num < arr[mid+1]:
                return(mid)
            else:
                p = mid+1
    return(q)

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    
    line = infile.readline()
    T = int(line)

    for t in range(1,T+1):
        line = infile.readline()
        N = int(line)

        line = infile.readline().strip('\n').split(" ")
        naomi = [float(el) for el in line]

        line = infile.readline().strip('\n').split(" ")
        ken = [float(el) for el in line]

        naomi_asc = sorted(naomi)
        ken_asc = sorted(ken)
        #print(naomi_asc)
        #print(ken_asc)
        # D War: Count number of winning pairs for Naomi
        dcount = 0
        while len(naomi_asc) > 0:
            closest = find_closest(naomi_asc[-1], ken_asc)
            #print(closest)
            if closest == -1:
                break
            else:
                dcount += 1
                del naomi_asc[-1]
                del ken_asc[closest]
        

        # War: Count number of winning pairs for Ken and subtract from N
        naomi_asc = sorted(naomi)
        ken_asc = sorted(ken)
        wcount = 0
        while len(ken_asc) > 0:
            closest = find_closest(ken_asc[-1], naomi_asc)
            #print(closest)
            if closest == -1:
                break
            else:
                wcount += 1
                del ken_asc[-1]
                del naomi_asc[closest]

        wcount = N - wcount
        outfile.write("Case #{0}: {1} {2}\n".format(t,dcount,wcount))
        print("Case #{0}: {1} {2}\n".format(t,dcount,wcount))

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()

    
