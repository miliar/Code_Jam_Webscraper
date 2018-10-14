import fileinput


for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue

    n = [int(c) for c in line.strip()]

    if n == list(sorted(n)):
        result = line.strip()
    else:
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if n[j] < n[i]:
                    stop_here = True
                    break
                elif n[j] > n[i]:
                    stop_here = False
                    break
            if stop_here:
                n[i] -= 1
                for j in range(i + 1, len(n)):
                    n[j] = 9
                result = int("".join(str(x) for x in n))
                break

    print("Case #{}: {}".format(e, result))
