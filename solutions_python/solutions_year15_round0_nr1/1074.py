f = open('A-large.in', 'r')
out = open('out-large.txt', 'w')
T = int(f.readline())

for case in range(T):
    line = f.readline()
    pattern = line.strip().split()
    max = int(pattern[0])

    audience = pattern[1]

    sum = 0
    invite = 0
    for i in range(max + 1):
        if (int(audience[i]) + sum) < i + 1:
            invite += 1#i + 1 - (int(audience[i]) + sum)
            sum += 1#i + 1 - (int(audience[i]) + sum)
        else:
            sum += int(audience[i])

    print(invite)
    out.write("Case #" + str(case + 1) + ": " + str(invite) + "\n")


