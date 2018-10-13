#!/usr/bin/env python

def convertTo9(N,i):
    for n in range(i+1):
        N[n] = 9

def solve(N):
    N.reverse()
    for i in range(len(N)-1) :
        if N[i] < N[i+1] :
            convertTo9(N,i)
            N[i+1] -= 1
        # print(i,d)
    
    N.reverse()
    return int(''.join(map(str,N)))


def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):
        
        # Read the data
        N = [int(s) for s in list(input())]
        # print(N)

        print("Case #{}: {}".format(case_counter, solve(N)))
        case_counter += 1


if  __name__ =='__main__':
    main()
