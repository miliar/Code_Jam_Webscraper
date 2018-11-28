def bisez(n, k):
    fstall = [(n, 1)]  # free stall in a row: (how many stalls are in the row, how many lines like of that type)
    while True:
        ftemp = []
        for x in fstall:
            k -= x[1]
            if k <= 0:
                m = int(x[0] / 2)
                if x[0] % 2 == 0:
                    return m, m - 1
                else:
                    return m, m

            m = int(x[0] / 2)
            if x[0] % 2 == 0:
                ftemp.append((m, x[1]))
                ftemp.append((m-1, x[1]))
            else:
                ftemp.append((m, x[1]*2))

            if len(ftemp) == 3:   # [(2,1),(1,1),  (1,2)] or [(2,2),  (2,1),(1,1)]...  ex: bisez(8,1) -> [(4,1),(3,1)] -> [(2,1),(1,1),  (1,2)]
                if ftemp[1][0] == ftemp[2][0]:
                    ftemp = [ftemp[0], (ftemp[2][0], ftemp[1][1]+ftemp[2][1])]
                else:
                    ftemp = [(ftemp[0][0], ftemp[0][1]+ftemp[1][1]),  ftemp[2]]

        fstall = ftemp


with open('C-small-2-attempt1.in', 'r') as f_in, open('out.txt', 'w') as f_out:
    t = int(f_in.readline())
    for i_, line in enumerate(f_in):
        n, k = [int(x) for x in line.split(" ")]
        # print("input#{}: {} {}".format(i_ + 1, n, k))

        f_out.write("Case #{}: {} {}\n".format(i_ + 1, *bisez(n, k)))
