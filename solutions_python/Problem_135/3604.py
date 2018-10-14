inptstr="""3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16"""

inpt = inptstr.split("\n")

def magic(inpt):
    w = open("small.out", 'w')
    for i in range(int(inpt[0])):
        j = i * 10 + 1
        n = int(inpt[j])
        m = int(inpt[j + 5])
        tmp1 = inpt[j + n].split(" ")
        tmp2 = inpt[j + m + 5].split(" ")

        found = 0
        for k in tmp1:
            if k in tmp2:
                found += 1
                nr = k
        if found:
            if found == 1:
                out = "Case #{0}: {1}".format(i + 1, nr)
            else:
                out = "Case #{0}: Bad magician!".format(i + 1)
        else:
            out = "Case #{0}: Volunteer cheated!".format(i + 1)
        w.write(out+'\n')
        
                
f = open("A-small-attempt0.in")

inpt = []
for line in f:
    inpt.append(line.strip())

f.close()

magic(inpt)


        
