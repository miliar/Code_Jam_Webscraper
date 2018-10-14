def read_input(fileName):
    fo = open(fileName, "r")
    content = fo.read().strip()
    fo.close()

    lines = content.split("\n")
    tc = int(lines[0].strip())
    lines = lines[1:]

    return(tc, lines)

file = "test.txt"
file = "test2.txt"
file = "small.in"
file = "large.in"
(tc, lines) = read_input(file)

l = 0
outfile = list()
for t in range(tc):
    (D, N) = lines[l].strip().split(" ")
    (D, N) = (float(D), int(N))
    l += 1
    horses = list()
    for i in range(N):
        (K, S) = lines[l].strip().split(" ")
        (K, S) = (float(K), float(S))
        l += 1
        horses.append((K,S))

    max_duration = float(0)

    for h in horses:
        time = (D - h[0])/h[1]
        if time > max_duration:
            max_duration = time
    result = round(D/max_duration, 6)
    outfile.append("Case #" + str(t+1) + ": " + str(result))

fo = open(file + ".out.txt", "w")
fo.write("\n".join(outfile))
fo.close()
