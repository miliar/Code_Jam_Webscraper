input = open("rn.in" , "r")
output = open("rn.out" , "w")

def variate(n):
    vars = []
    n = str(n)
    for l in range(len(n) - 1):
        n = n[-1] + n[:-1]
        vars.append(int(n))
    return set(vars)

cases = int(input.readline())

for i in range(1, cases + 1):
    count = 0
    (f, l) = [int(x) for x in input.readline().split()]
    for j in range(f, l + 1):
        vars = variate(j)
        for k in vars:
            if k >= f and k <= l and k != j:
                count += 1
    count = count/2
    print "Case #" + str(i) + ": " + str(count)
    output.write("Case #" + str(i) + ": " + str(count) + "\n")
input.close()
output.close()
