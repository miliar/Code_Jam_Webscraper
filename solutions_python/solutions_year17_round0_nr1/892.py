
def solve(s,k):
    cake = []
    for i in range(len(s)):
        if s[i] == '+':
            cake.append(1)
        else:
            cake.append(0)
    step = 0
    for i in range(len(cake)-k+1):
        if cake[i] == 0:
            for j in range(k):
                cake[i+j] = 1 - cake[i+j]
            step += 1
    if 0 in cake:
        return 'IMPOSSIBLE'
    else:
        return str(step)
    

with open("in","r") as reader:
    with open("out",'w') as writer:
        t = int(reader.readline())
        for i in range(t):
            s , k = map(str, reader.readline().split())
            writer.write("Case #" + str(i+1) + ": " + solve(s,int(k))+ "\n")
