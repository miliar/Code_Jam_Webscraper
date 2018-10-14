#We represent s as a list of 0s and 1s. 0s are blank, 1s are happy. k is the length of the pancake flipper.
def f(l, k):
    if len(l) == 0:
        return 0
    elif len(l) < k:
        return (sum(l) == len(l))
    elif len(l) == k:
        if sum(l) == 0:
            return 1
        elif sum(l) == len(l):
            return 0
        else:
            return "IMPOSSIBLE"
    else:
        flips = 0
        for i in range(len(l)-k+1):
            if l[i] == 0:
                for j in range(i,i+k):
                    l[j] = 1-l[j]
                flips += 1
        if sum(l) == len(l):
            return flips
        else:
            return "IMPOSSIBLE"

def convert(s):
    l = []
    for i in s:
        if i == "+":
            l.append(1)
        else:
            l.append(0)
    return l

r = open("i.in")
w = open("o.out", "w")
for i in range(int(r.readline())):
    inp = r.readline().split()
    l, k = convert(inp[0]), int(inp[1])
    w.write("Case #" + str(i+1) + ": " + str(f(l,k)) + "\n")
