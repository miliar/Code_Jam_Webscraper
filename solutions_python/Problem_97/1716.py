inp = open("input.txt", "r")
out = open("output.txt", "w")

line = inp.readline()
num_lines = int(line)
case = 1
for line in inp:
    line = line.split()
    if len(line) < 2:
        continue
    low, high = int(line[0]), int(line[1])
    found = 0
    leaddigit = int(str(low)[0])
    lenlow = len(line[0])
    if len(line[0]) == 1:
        out.write("Case #{0}: 0\n".format(case))
        case += 1
        continue
    for i in xrange(low, high + 1):
        done = {}
        num = list(str(i))
        l = len(num)
        possibles = []
        for j in xrange(1, l):
            if num[j] == '0':
                continue
            if num[j] > leaddigit and l > lenlow:
                continue
            m = int("".join(num[j:]) + "".join(num[:j]))
            n = i
            if done.get(m, 0) and done.get(n, 0):
                continue
            if low <= m and m <= n and n <= high and m != n:
                found += 1
            done[m] = 1
            done[n] = 1
    out.write("Case #{0}: {1}\n".format(case, found))
    case += 1
