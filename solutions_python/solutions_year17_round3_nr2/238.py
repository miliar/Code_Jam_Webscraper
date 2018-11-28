
def solve(C, J, C1):
    if C + J == 1 or (C == 1 and J == 1):
        return 2
    C1.sort()
    print(C1[1][1] - C1[0][0])
    if C1[1][0] - C1[0][1] >= 720:
        return 2
    if C1[1][1] - C1[0][0] > 720:
        return 4
    else:
        return 2


with open("in","r") as reader, open("out",'w') as writer:
    t = int(reader.readline())
    for i in range(t):
        C, J = map(int, reader.readline().split())
        C1, J1 = [], []
        for j in range(C+J):
            s, e = map(int, reader.readline().split())
            C1.append((s,e))
        writer.write("Case #{}: {}\n".format(i+1, solve(C, J, C1)))
