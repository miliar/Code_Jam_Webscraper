with open("B-small-attempt0.in") as f:
    with open("output.txt", "w") as g:
        t = int(f.readline().strip())
        for i in range(1, t + 1):
            # print("i = {}".format(i))
            [ac, aj] = map(int, f.readline().split())
            
            # store as [start, end, duration]
            cd = [None] * ac
            for j in range(ac):
            	[ci, di] = map(int, f.readline().split())
            	cd[j] = (ci, di, di-ci)
            jk = [None] * aj
            for j in range(aj):
            	[ji, ki] = map(int, f.readline().split())
            	jk[j] = (ji, ki, ki-ji)

            if len(cd) == 2:
                # check if there's a gap between the two which is 12 hours long
                if (cd[0][0] - cd[1][1]) % 1440 < 720 and (cd[1][0] - cd[0][1]) % 1440 < 720:
                    # no gap
                    g.write("Case #{}: {}\n".format(i, 4))
                else:
                    g.write("Case #{}: {}\n".format(i, 2))
            elif len(jk) == 2:
                # check if there's a gap between the two which is 12 hours long
                if (jk[0][0] - jk[1][1]) % 1440 < 720 and (jk[1][0] - jk[0][1]) % 1440 < 720:
                    # no gap
                    g.write("Case #{}: {}\n".format(i, 4))
                else:
                    g.write("Case #{}: {}\n".format(i, 2))
            else:
                g.write("Case #{}: {}\n".format(i, 2))
