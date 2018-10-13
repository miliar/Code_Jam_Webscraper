def getIndexFirstMinus(l):
    for i in range(len(l)):
        if l[i]=='-':
            return i
    return -1

def flip(l,index,k):
    try:
        print(l,index,k)
        for i in range(index, index+k):
            l[i] = '-' if l[i]=='+' else '+'
        return True
    except IndexError:
        return False

def solve(l, k):
    flips = 0 
    while True:
        index = getIndexFirstMinus(l)
        if index == -1:
            return str(flips)
        if (flip(l,index,k)):
            flips+=1
        else:
            return "IMPOSSIBLE"



import sys
L = list(open(sys.argv[1], 'r'))
L = L[1:]
f = open(sys.argv[2], 'w')
i = 1 
for l in L:
    l = l.rstrip().split(" ")
    k = int(l[1])
    f.write("Case #" + str(i)+": " + solve(list(l[0]), k) + "\n")
    i+=1