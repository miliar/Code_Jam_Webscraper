# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def flipStack(stack, k, index):
    newStack = stack[:index]
    for c in range(index, index+k):
        if stack[c] == "+":
            newStack  += "-"
        else:
            newStack += "+"
    newStack += stack[index+k:]
    return newStack

def solve(stack, k):
    flips = 0
    for i in range(len(stack)-k+1):
        if stack[i] == "-":
            stack = flipStack(stack,k,i)
            flips += 1
    if stack != ("+"*len(stack)):
        return "IMPOSSIBLE"
    return flips


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    stack, k = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    moves = solve(stack, int(k))
    print("Case #{}: {}".format(i, moves))
    # check out .format's specification for more formatting options

