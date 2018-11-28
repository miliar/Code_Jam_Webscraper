[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

nope = [("r", "o"), ("r", "v"), ("o", "y"), ("y", "g"), ("g", "b"), ("b", "v")]
for case in range(cases):
    # solving logic goes here
    (n, r, o, y, g, b, v) = [int(x) for x in raw_input().strip().split()]
    if o != 0 or g != 0 or v != 0:
        print "!!!!!!!"
        break

    colors = {"r": r, "y": y, "b": b}
    maxcolor = "r"
    for c in colors:
        if colors[c] > colors[maxcolor]:
            maxcolor = c
    othercolors = colors.keys()
    othercolors.remove(maxcolor)
    if sum(colors[c] for c in othercolors) < colors[maxcolor]:
        res = "IMPOSSIBLE"
    else:
        stalls = [maxcolor] * colors[maxcolor]
        if colors[othercolors[0]] > colors[othercolors[1]]:
            nextmax = othercolors[0]
            last = othercolors[1]
        else:
            nextmax = othercolors[1]
            last = othercolors[0]

        firststage = (colors[last] - (colors[maxcolor]-colors[nextmax]))
        secondstage = (colors[nextmax] - firststage)
        thirdstage = colors[maxcolor] - secondstage - firststage
        stalls = [maxcolor, nextmax, last] * firststage
        stalls += [maxcolor, nextmax] * secondstage
        stalls += [maxcolor, last] * thirdstage

        res = ''.join(stalls).upper()

    s = "Case #"+str(case+1)+": "+res+'\n'
    out.write(s)
    print(s)
