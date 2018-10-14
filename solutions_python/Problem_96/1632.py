with open("b-large.in", "r") as fin:
    with open("b-small.out", "w") as fout:
        n = int(fin.readline())
        for case in range(1, n + 1):
            line = fin.readline()
            parts = [int(x) for x in line.split(" ")]
            m = parts[0]
            s = parts[1]
            p = parts[2]
            scores = parts[3:]
            count = 0
            for i in range(m):
                if scores[i] >= p * 3 - 2:
                    count += 1
                elif scores[i] >= (1 if p == 1 else p * 3 - 4) and s > 0:
                    count += 1
                    s -= 1
            fout.write("Case #" + str(case) + ": " + str(count) + "\n")
