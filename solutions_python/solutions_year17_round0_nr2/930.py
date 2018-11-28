
def solve(s):
    if len(s) > 1 and s[0] > s[1]:
        return chr(ord(s[0]) - 1) + '9'*(len(s)-1)
    else:
        return s

def solver(s):
    for i in range(len(s)-1, -1, -1):
        s = s[:i] + solve(s[i:])
    return int(s)

with open("in","r") as reader:
    with open("out",'w') as writer:
        t = int(reader.readline())
        for i in range(t):
            s = int(reader.readline())
            writer.write("Case #" + str(i+1) + ": " + str(solver(str(s))) + "\n")
