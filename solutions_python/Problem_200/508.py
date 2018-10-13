# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

DEBUG=0

# def flip_pancakes(pancakes, pos, k):
#     for i in range(pos, pos + k):
#         if pancakes[i] == "+":
#             pancakes[i] = "-"
#         else:
#             pancakes[i] = "+"

def printd(*arg):
    if DEBUG == 1:
        print("---",arg)
        
    

t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    num_s = input()
    printd(num_s)
    #num = int(num_s)
    num_a = list(num_s)
    n=len(num_a)
    for i in range(0,n):
        num_a[i] = int(num_a[i])
    tidy = False
    while (not tidy):
        tidy = True
        for i in range(0,n-1):
            if(num_a[i]>num_a[i+1]):
                tidy = False
                printd("invert {} and {}".format(num_a[i],num_a[i+1]))
                num_a[i] -= 1
                for j in range(i+1, n):
                    num_a[j] = 9
                printd(num_a)
                break
    last_tidy_s=""
    for s in num_a:
        last_tidy_s += str(s)
    last_tidy=int(last_tidy_s)
    print("Case #{}: {}".format(case_num,last_tidy))

  
