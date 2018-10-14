f = open("C-small-attempt0.in")

T = int(f.readline())

out = open("C-small.out", 'w')

for i in range(T):
    line = f.readline().strip().split()

    A = int(line[0])
    B = int(line[1])

    total = 0

    for a in range(A, B):
        for b in range(a+1, B+1):
            na = str(a)
            for c in str(a):
                na = na[1:len(na)] + na[0]
                if na == str(b):
                    total += 1
                    break

    out.write("Case #" + str(i+1) + ": " + str(total) + '\n')

out.close()
f.close()