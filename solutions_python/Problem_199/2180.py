def flips(pancakes, k):
    count = 0
    pancakes = [c=='+' for c in pancakes]
    for i in range(len(pancakes) - k + 1):
        if not pancakes[i]:
            count += 1
            for j in range(i, i+k):
                pancakes[j] = not pancakes[j]
    if False in pancakes:
        return "IMPOSSIBLE"
    else:
        return count

f = open("A-large.in", "r")

fout = open("quala.out", "w")

f.readline() # discard number of cases

for num, line in enumerate(f):
    pancakes, k = line.split()
    res = flips(pancakes, int(k))
    fout.write("Case #{}: {}\n".format(num+1, res))