from operator import itemgetter

with open("B-small-attempt0.in", "r") as inp:
    with open("B-small-attempt0.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            n, r, o, y, g, b, v = [int(x) for x in inp.readline().split()]
            colors_list = [r, y, b]
            colors_dict = {"R": r, "Y": y, "B": b}
            if colors_list.count(0) == 2:
                for color, occ in colors_dict.items():
                    if occ > 1:
                        outp.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")
                        break
                    elif occ == 1:
                        outp.write("Case #" + str(i+1) + ": " + color + "\n")
                        break
                done = True
            elif colors_list.count(0) == 1:
                colors_list.remove(0)
                if colors_list[0] != colors_list[1]:
                    outp.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")
                else:
                    letters = ""
                    times = 0
                    for color, occ in colors_dict.items():
                        if occ > 0:
                            letters += color
                            times = occ
                    outp.write("Case #" + str(i+1) + ": " + letters*times + "\n")
            else:
                letters = ""
                sorted_colors = [list(x) for x in sorted(colors_dict.items(), key=itemgetter(1), reverse=True)]
                while sorted_colors[1][1] > sorted_colors[2][1]:
                    letters += sorted_colors[0][0] + sorted_colors[1][0]
                    sorted_colors[0][1] -= 1
                    sorted_colors[1][1] -= 1
                if sorted_colors[0][1] == sorted_colors[1][1]:
                    letters += (sorted_colors[0][0] + sorted_colors[1][0] +
                                sorted_colors[2][0]) * sorted_colors[0][1]
                    outp.write("Case #" + str(i+1) + ": " + letters + "\n")
                else:
                    done = False
                    while sorted_colors[1][1] > 0:
                        letters += (sorted_colors[0][0] + sorted_colors[1][0] +
                                    sorted_colors[0][0] + sorted_colors[2][0])
                        sorted_colors[0][1] -= 2
                        sorted_colors[1][1] -= 1
                        sorted_colors[2][1] -= 1
                        if sorted_colors[0][1] == sorted_colors[1][1]:
                            letters += (sorted_colors[0][0] + sorted_colors[1][0] +
                                sorted_colors[2][0]) * sorted_colors[0][1]
                            outp.write("Case #" + str(i+1) + ": " + letters + "\n")
                            done = True
                    if not done:
                        outp.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")
