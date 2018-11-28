import math

def Solve(w, h):
    sum = 0
    for i in range(len(w)-h+1):
        if (w[i] == '-'):
            w = reverse (w, i, h)
            sum += 1
    for i in range(len(w)-h+1,len(w)):
        if (w[i] == '-'):
            return "IMPOSSIBLE"
    return sum

def reverse (w, i, h):
    for tt in range(i, i+h):
        if (w[tt] == '-'):
            w[tt] = '+'
        else:
            w[tt] = '-'
    return w

input = open('task1.in','r')
output = open('output1.txt','w+')
T = int(input.readline())
for t in range(T):
    w, h = input.readline().split()
    w = list(w)
    h = int(h)
    output.write("Case #{}: {}\n".format(t + 1, Solve(w, h)))