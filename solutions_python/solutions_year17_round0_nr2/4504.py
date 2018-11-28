# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = list(input())
    #print("".join(N))
    for index in reversed(range(len(N)-1)):
        if int(N[index]) > int(N[index+1]):
            N[index] = str(int(N[index])-1)
            for aux in range(index+1,len(N)):
                N[aux] = "9"
            index=0
    print("Case #{}: {}".format(i, int("".join(N))))
    # check out .format's specification for more formatting options
