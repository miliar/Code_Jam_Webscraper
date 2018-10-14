infile = "C-small-attempt0.in"
#infile = "input"
f = open(infile, "r")
f_out = open("output", "w")
num = int(f.readline().strip())

for i in range(num):
    l = f.readline().strip().split()
    A = int(l[0])
    B = int(l[1])

    n = [1,4,9,121,484]
    numbers = 0
    if A not in n:
        n.append(A)
    else:
        numbers += 1
    if B not in n:
        n.append(B)
    else:
        numbers += 1
    n.sort()
    numbers += n.index(B)-n.index(A)-1
    f_out.write("Case #{0}: {1}\n".format(i+1, numbers))

f.close()
f_out.close()


