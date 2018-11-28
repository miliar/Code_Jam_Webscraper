def tidy(N):
    isTidy = True
    n = str(N)
    l = len(n) - 1
    k = 0
    
    while k < l:
        if int(n[k]) > int(n[k+1]):
            isTidy = False
            break
        k += 1
        
    if isTidy:
        print(N)
    else:
        tidy(N-1)

import sys
file1 = open("B-small-attempt3.in","r")
with open("B-small-attempt3.out","w") as file2:
    sys.stdout = file2
    T = int(file1.readline())
    i = 0
    for line in file1:
        i += 1
        print("Case #%d: "% i,end ="")
        tidy(int(line))

