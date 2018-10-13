import sys
import math

def solve(n):
    s = [int(i) for i in n]
    s.reverse()
    lowest = 9
    
    for i in range(len(s)):
        # if i == len(s)-1:
            # return int(''.join([str(x) for x in s][::-1]))
        if i < len(s)-1:
            if s[i] < s[i+1] or s[i] == 0 or s[i]> lowest:
                s[i] = lowest
                s[i+1]-=1
            else:
                lowest = s[i]
        if i == len(s)-1:
            # print s[i]
            if s[i] > lowest or s[i] == int(n[0])-1:
                s[i] = int(n[0])-1
                for j in range(len(s)-1):
                    s[j] = 9
    return int(''.join([str(x) for x in s][::-1]))


if __name__ == '__main__':
    f = open(sys.argv[1])
    T = int(f.readline())

    for i in range(T):
        print "Case #{}: {}".format(i+1, solve(f.readline().strip()))