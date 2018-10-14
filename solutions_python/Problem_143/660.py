from sys import stdin

test_cases = int(stdin.readline())

for i in range(test_cases):
    ting = stdin.readline()
    ting = ting.split()
    A = int(ting[0]) 
    B =int(ting[1])
    K =int(ting[2])
    total = 0
    for n in range(A):
        for m in range(B):
            if (n&m < K):
                total += 1
    print("Case #" + str(i+1) + ": " + str(total))
