from sys import argv

script, filename = argv

txt = open(filename)
outfile = open("output.txt", 'w')

T = int(txt.readline())

for i in range(0,T):
    ints = []
    for val in txt.readline().split():
        ints.append(int(val))
    N = ints[0]
    S = ints[1]
    p = ints[2]
    total = 0
    for j in range(0,N):
        if (ints[3+j] >= 3*p-2) and (ints[3+j] >= p) :
            total += 1
        elif (ints[3+j] >= 3*p-4) and (S >= 1)and (ints[3+j] >= p):
            total += 1
            S -= 1
    
    outfile.write("Case #")
    outfile.write(str(i+1))
    outfile.write(": ")
    outfile.write(str(total))
    outfile.write("\n")
    
txt.close()
outfile.close()
