# python2
import sys
import math


def copy_array(A):
    B = []
    for i in range(len(A)):
        B.append(A[i])
    return B


def compare_string(A, B):
    S_A = ""
    S_B = ""
    for c in A:
        S_A = S_A + c
    for c in B:
        S_B = S_B + c

    if (S_A == S_B):
        return 0
    else:
        if (S_A < S_B):
            return -1
        else:
            return 1
        
    
class main():
    T = int(sys.stdin.readline().rstrip())
    
    for t in range(T):
        line = sys.stdin.readline().rstrip()
        num = []
        for c in str(int(line)):
            num.append(c)

        n = len(num)
        last = []
        for i in range(n):
            last.append('1')

        if (compare_string(last, num) == 1):
            temp = ""
            for i in range(n-1):
                temp = temp + "9"
            print "Case #" + str(t+1) + ": " + temp
        else:
            for i in range(n):
                temp = copy_array(last)
                digit_i = ord(temp[i])-48
                
                for j in range(digit_i+1, 10):      # update the i-th digit
                    for k in range(i, n):
                        temp[k] = chr(j+48)
                    if (compare_string(temp, num) != 1):
                        last = copy_array(temp)
                    else:
                        break
                
            result = "".join(x for x in last)            
            print "Case #" + str(t+1) + ": " + result
