data = open('a.in', 'r').readlines()
data = data[1:]

def flip(part):
    res = []
    for v in part:
        res += ["+"] if v == "-" else ["-"]
    return res
output = ""
for i in range(len(data)):
    result, size = data[i].split(" ")
    size = int(size)
    result = list(result)
    flips = 0
    for j in range(len(result) - (size-1)):
        if result[j] == "-":
            flips += 1
            result[j:j+size] = flip(result[j:j+size])
    if not "-" in result:
        output += "Case #{}: {}\n".format(i+1, flips)
    else:
        output += "Case #{}: IMPOSSIBLE\n".format(i + 1)

f = open('a.out', 'w')
f.write(output)
