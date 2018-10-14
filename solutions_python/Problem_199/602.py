import fileinput


for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue

    ps, k = line.strip().split()
    ps = [0 if c == '-' else 1 for c in ps]
    k = int(k)

    result = 0
    for i in range(len(ps)):
        if not ps[i]:
            if i + k > len(ps):
                result = "IMPOSSIBLE"
                break
            else:
                for j in range(i, i + k):
                    ps[j] = (ps[j] + 1) % 2
                result += 1

    print("Case #{}: {}".format(e, result))
