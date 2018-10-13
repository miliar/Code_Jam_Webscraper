import sys

iname = sys.argv[1]
oname = iname.rstrip('in') + "out"
result = ""
with open(iname, "rb") as f:
    cases = int(f.readline().strip())
    for case in range(cases):
        line = f.readline().strip().split()
        pancakes = [i == '+' for i in line[0]]
        k = int(line[1])
        count = 0
        for i in range(len(pancakes) - k + 1):
            if not pancakes[i]: 
                for j in range(i, i + k):
                    pancakes[j] = not pancakes[j]
                count += 1 
        if all(pancakes):
            result += "Case #%d: %d\n" % (case + 1, count)
        else:
            result += "Case #%d: IMPOSSIBLE\n" % (case + 1)
with open(oname, "wb") as f:
    f.write(result)
