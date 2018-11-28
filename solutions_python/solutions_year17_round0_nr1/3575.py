L = []
K = []

def flip(ls, ch, f):
    if (len(ls) - ch) >= f:
        new_ls = list(ls)
        for i in range(f):
            if ls[ch] == "-":
                new_ls[ch] = "+" 
                pass
            else:
                new_ls[ch] = "-"
            ch += 1
        ls = "".join(new_ls)
    return ls
"""
with open("A-small-attempt1.in", "r") as f:
    comp = f.readlines()
"""
t = int(input()) 

for i in range(1, t+1):
    g = input().split(" ")
    L.append(g[0])
    K.append(int(g[1]))
    
for j in range(len(L)):
    count = 0
    for k in range(len(L[j])):
        if L[j][k] == "-":
            count += 1
            L[j] = flip(L[j], k, K[j])
    count = str(count)
    if "-" in L[j]:
        count = "IMPOSSIBLE"

    print("case #" + str(j+1)+ ": " + count)