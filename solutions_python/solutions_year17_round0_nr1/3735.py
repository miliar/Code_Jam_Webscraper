f = open("A-large.in","r")
lines = [line.split() for line in f.readlines()]
T = lines[0]

def solve(string,k):
    num = 0
    while len(string) >= k:
        if string[0] == "+":
            string = string[1:]
        else:
            flipped = flip(string[0:k])
            num += 1
            string = flipped + string[k:]
    for char in string:
        if char == "-":
            return -1
    return num

def flip(pancakes):
    out = ""
    for char in pancakes:
        if char == "+":
            out += "-"
        else:
            out += "+"
    return out

g = open("A-large.out","w")
for i in range(1,len(lines)):
    case = lines[i]
    string = case[0]
    k = int(case[1])
    n = solve(string, k) 
    if n == -1:
        g.write("Case #{0}: IMPOSSIBLE\n".format(i))
    else:
        g.write("Case #{0}: {1}\n".format(i,n))
        
f.close()
g.close()
