def read(f):
    return f.readline().strip()
with open("A-small-attempt1.in") as infile:
    n = int(read(infile))
    for case in range(1,n+1):
        a1 = int(read(infile))
        for i in range(1,5):
            line = read(infile).split()
            if i == a1:
                ans1 = line
        a2 = int(read(infile))
        for i in range(1,5):
            line = read(infile).split()
            if i == a2:
                ans2 = line
        matches = list(set(ans1).intersection(set(ans2)))
        if len(matches) == 0:
            print("Case #{}: {}".format(case,"Volunteer cheated!"))
        elif len(matches) == 1:
            print("Case #{}: {}".format(case,matches[0]))
        else:
            print("Case #{}: {}".format(case,"Bad magician!"))

