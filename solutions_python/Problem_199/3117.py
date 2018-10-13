# pancake.py
def test(c, k): # cake, flipper

    x = 0
    k = int(k)
    l = list(c)
    for i in range(len(l) - k + 1):
        if l[i] == "-":
            for j in range(k):
                l[i + j] = flip(l[i + j])
            x += 1
    for i in range(k):
        if l[-i] == "-":
            return "IMPOSSIBLE"
    return x

def flip(p):
    if p == "-": p = "+"
    else: p = "-"
    return p

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
 	c, k = input().split(" ")
 	print("Case #{}: {}".format(i, test(c, k)))
