#!/usr/bin/env python
import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())    

    for i in range(T):
        line = sys.stdin.readline()
        line.replace("\n", "")
        
        numbers = list(map(int, line.split()))

        N = numbers[0]
        S = numbers[1]
        p = numbers[2]

        threshold_normal_score = 2*max((p-1), 0) + p
        threshold_surprising_score = 2 * max((p-2), 0) + p
        
        count = 0
        surprising_count = 0

        for j in range(N):
            score_sum = numbers[3+j]

            if score_sum >= threshold_normal_score:
                count += 1
            elif (score_sum >= threshold_surprising_score) and (surprising_count < S):
                count += 1 
                surprising_count += 1
                

        print ("Case #{0}: {1}".format(i+1, count))

