# Google Code Jam 2014 Qualification Round
# Problem B
# Shaotong Wang

fin = open('B_test.in', 'r')
fout = open('B_test.out', 'w')

num_cases = int(fin.readline())

for case in range(1,num_cases+1):
    c, f, x = map(float, fin.readline().split())
    t = 0.0
    cps = 2.0

    while (x-c)/cps > x/(cps+f):
        t += c/cps
        cps += f

    t += x/cps
    
    fout.write("Case #" + str(case) + ": " + str(t) + "\n")

fin.close()
fout.close()

