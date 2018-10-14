import numpy as np

def notAscending(A):
    return np.array_equal(A, sorted(A)) == False

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    n=n[0]
    A = list(map(int, str(n)))
    while(notAscending(A)):
        for i in range(len(A) -1 ,0, -1):
            if(A[i] == 0):
                for k in range(i, len(A)):
                    A[k] = 9
                A[i-1] -= 1
            if(A[i] < A[i-1]):
                for k in range(i, len(A)):
                    A[k] = 9
                A[i-1] -= 1
                    
    
    A = ''.join(list(map(str, A)))
    A = int(A)
    print("Case #{}: {}".format(j, A))
    # check out .format's specification for more formatting options