from sys import stdin

T = int(stdin.readline())
base = ord('0')

for i in range(T):
    L = stdin.readline().split()
    Smax = int(L[0])
    standing = 0
    ans = 0
    for j in range(len(L[1])):
        if standing < j:
            ans += (j - standing)
            standing = j
        standing += ord(L[1][j]) - base
        #print(L[1][j],end='')

    print('Case #' + str(i+1) + ": " + str(ans))        
    
