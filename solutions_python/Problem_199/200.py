
def flip(s, pos, len):
    for i in range(pos,pos+len):
        s[i] = "+" if s[i] == "-" else "-"
    return s

def solve(s,k):
    """ Just to a greedy algo"""

    flips = 0

    s = list(s)

    i = 0
    while i <= len(s)-k:
        if s[i] == '-':
            s = flip(s,i,k)
            flips += 1
            #print(flips,s)
        i += 1
    #print(s,flips)
    if "-" in s:
        return "IMPOSSIBLE"
    else:
        return flips

T = int(input())
for t in range(T):
    s,k = input().split(" ")
    k = int(k)
    print("Case #{0}: {1}".format(t+1,solve(s,k)))