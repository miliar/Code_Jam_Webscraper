import sys

def solveCase(t):
    n = list(map(int, list(sys.stdin.readline().strip())))

    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            
            for j in range(i + 1, len(n)):
                n[j] = 9

    num = int("".join(map(str, n)))
    print("Case #{}: {}".format(t, num))



    

T = int(sys.stdin.readline())

for t in range(T):
    solveCase(t + 1)
