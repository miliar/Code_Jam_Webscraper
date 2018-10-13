# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

DEBUG=0

def flip_pancakes(pancakes, pos, k):
    for i in range(pos, pos + k):
        if pancakes[i] == "+":
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"

def printd(*arg):
    if DEBUG == 1:
        print(arg)
        
    

t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    pancakes_s, k_s = input().split(" ")
    pancakes=list(pancakes_s)
    printd(pancakes)
    k = int(k_s)
    n=len(pancakes_s)
    flips=0
    for j in range(0,n-k+1):
        printd("loop: {}, {}".format(j,str(pancakes)))
        if pancakes[j] == "-":
            flip_pancakes(pancakes,j,k)
            flips += 1
            printd("flip@{}".format(j))
    for j in range(0,n):
        if pancakes[j] == "-":
            flips = -1
            break
    if flips == -1:
        print("Case #{}: {}".format(case_num, "IMPOSSIBLE" ))
    else:
        print("Case #{}: {}".format(case_num, flips ))

  
