# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math
import string

f = open("C:\Users\Jafar\Downloads\A-large.in",'r')
g = open("Answer.txt", 'w')
def solve():
    #Here will be function
    a = 1
#end_def
t = int(f.readline())  # read a line with a single integer
#t = 5
for z in range(1, t + 1):
    R, C = map(int, f.readline().strip().split(" "))
    #R, C = 3, 4
    arr = []
    for i in range(R):
        arr.append([ch for ch in f.readline().strip()])
    #end_for
    count = 0
    for i in range(R):
        if sum([(1 if ch== "?" else 0) for ch in arr[i]]) == C:
            count += 1
            continue
        #end_if
        print count
        ind = 0
        while arr[i][ind] == "?":
            ind += 1
        #end_if
        ch = arr[i][ind]
        for j in range(C):
            if arr[i][j] != "?":
                ch = arr[i][j]
            for s in range(count+1):
                print i, j, s, ch
                arr[i-s][j] = ch
            #end_if
            print ch, count
        count = 0
    #end_if
    for i in range(R-count, R):
        for j in range(C):
            arr[i][j] =arr[R-count-1][j]
    #end_for


    g.write("Case #{}:\n".format(z))
    for i in range(R):
        g.write("".join(arr[i] + ["\n"]))
#end_for
