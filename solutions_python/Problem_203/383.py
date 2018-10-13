f = open("A-large.in", "r")
g = open("output.txt","w")
number = int(f.readline())
for i in range(number):
    s = f.readline()
    s = s.split()
    r = int(s[0])
    c = int(s[1])
    g.write("Case #" + str(i + 1)+":"+"\n")
    lastline = ""
    count = 1
    for j in range(r):
        s = list(f.readline())
        current = "?"
        for k in range(c):
            if s[k] != "?":
                current = s[k]
            else:
                s[k] = current
        if current == "?":
            if lastline == "":
                count += 1
            else:
                g.write(lastline)
        else:
            for k in range(c - 1, -1, -1):
                if s[k] != "?":
                    current = s[k]
                else:
                    s[k] = current
            lastline = ("".join(s))
            for l in range(count):
                g.write("".join(s))
                count = 1
