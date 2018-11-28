filename = r"F:\Nir\Downloads\A-large.in"
output_file = r"F:\Nir\Downloads\A-large.out"


def solve(input):
    s, k = input.split(" ")
    k = int(k)
    l = [(True if v=="+" else False) for v in s]
    counter = 0
    for i in range(len(s)-k+1):
        if not l[i]:
            counter+=1
            #flip all
            for j in range(i,i+k):
                l[j] = not l[j]
    if l.count(False) != 0:
        return "IMPOSSIBLE"
    return str(counter)


inp = open(filename, "r")
s = inp.read().split("\n")
inp.close()
res = ""

t = int(s[0])
for i, input in enumerate(s[1:-1]):
    res += "Case #{}: {}\n".format(i+1,solve(input))

out = open(output_file, "w")
out.write(res)
out.close()