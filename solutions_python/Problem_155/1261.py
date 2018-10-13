data = open("inputA.txt")
output = open("outputA.txt", "w")
T = int(data.readline())
print(T)
for t in range(T):
    line = data.readline()
    shyest = int(line[0])
    shy_levels = [int(x) for x in line.strip()[2:]]
    current_count = 0
    extras_needed = 0
    for i in range(shyest + 1): #i is current shy level to check
        if current_count >= i:
            current_count += shy_levels[i]
        else:
            current_count += shy_levels[i] + 1
            extras_needed += 1
    output.write("Case #%d: %d\n" % (t+1, extras_needed))
output.close()
