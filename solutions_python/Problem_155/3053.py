def execute(filename):
    output = ""

    with open(filename, "r") as f:
        lines = [l.strip() for l in f][1:]
        for i, line in enumerate(lines):
            s = line.split(" ")[1]

            needed = 0
            sofar = 0

            for j, x in enumerate(s):
                x = int(x)

                if j != 0 and sofar + needed < j:
                    needed += (j - sofar - needed)
                sofar += x

            output += "Case #%s: %d" % (i+1, needed) + "\n"

    with open("output.txt", "w") as f:
        f.write(output)

filename = "A-large.in.txt"
execute(filename)
