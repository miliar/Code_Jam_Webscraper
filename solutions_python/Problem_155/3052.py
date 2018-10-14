with open("A-1.in", "r") as i:
    with open("A-large.out", "w") as o:
        c = 0
        for x in i:
            if c != 0:
                standing, friends = 0, 0
                s = [int(a) for a in x.split()[1]]
                for y in range(len(s)):
                    f = 0
                    if y > standing:
                        f = y - standing
                    friends += f
                    standing += f + s[y]
                o.write("Case #{0}: {1}\n".format(c, friends))
            c += 1
