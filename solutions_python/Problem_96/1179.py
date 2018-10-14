f = open("B-large.in")

T = int(f.readline())

out = open("B-large.out", 'w')

for i in range(T):
    out.write("Case #" + str(i+1) + ": ")

    line = f.readline().strip().split()

    maxi = 0

    N = int(line[0])
    S = int(line[1])
    p = int(line[2])

    scores = [int(line[j]) for j in range(3, len(line))]

    for t in scores:
        if t >= p*3-2:
            maxi += 1
        
        else:
            if t >= p*3 - 4 and S > 0 and p*3 - 4 > 0:
                maxi += 1
                S -= 1

    out.write(str(maxi) + "\n")

out.close()
f.close()

        