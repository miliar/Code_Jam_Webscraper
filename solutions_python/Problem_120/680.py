input = open("A-small-attempt0.in","r")
output = open("output","w")

input.readline()
case = 1
for line in input:
    r,t = map(int,line.strip().split())
    n = 0
    while t >= (2 * r + 1):
        t -= 2 * r + 1
        r += 2
        n += 1
    output.write("Case #{}: {}\n".format(case ,n))
    case += 1

input.close()
output.close()
