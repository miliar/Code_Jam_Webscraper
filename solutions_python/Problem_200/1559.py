import sys

def maxtidy(stev):
    """
    Returns the maximal tidy number that is not grater than n
    """
    n = len(stev)
    index = None
    if n == 1:
        return stev
    for i in range(n-1):
        if int(stev[i]) > int(stev[i+1]):
            index = i
            break
    if index is None:
        return stev
    while int(stev[index])-1 < int(stev[index-1]) and index > 0:
        index -= 1
    if index < 0:
        return ("9"*(n-1))
    if int(stev[index])-1 == 0:
        return ("9"*(n-1))
    else:
        return str(stev[:index])+str(int(stev[index])-1)+("9"*(n-index-1))

# print(maxtidy("101"))


T = int(sys.stdin.readline())
res = ""
for k in range(T):
    i = sys.stdin.readline()
    i = i.strip()
    res1 = maxtidy(i)
    res1 = "Case #{0}: {1}".format(k+1,res1)
    print(res1)
    res+= (res1+"\n")
with open("tiny_LARGE.out","w") as izhod:
    izhod.write(res)
