import math
import heapq
import copy
import itertools



            
    

def main():
    ifile = open('a.in', 'r')
    ofile = open('a.out', 'w')

    
    T = int(ifile.readline().strip())
    for case in range(1, T+1):
        N, X = [int(x) for x in ifile.readline().split()]
        S = sorted([int(x) for x in ifile.readline().split()])

        res, counter  = 0, 0
        ptr1, ptr2 = 0, N-1
        while counter < N:
            if S[ptr1] + S[ptr2] <= X:
                res+= 1
                counter += 2
                ptr1 +=1
                ptr2 -=1
            else:
                res+= 1
                counter += 1
                ptr2 -= 1        
        
        print(res)
        ofile.write('Case #%d: %d\n' %(case, res))

        

if __name__ == "__main__":
    main()
