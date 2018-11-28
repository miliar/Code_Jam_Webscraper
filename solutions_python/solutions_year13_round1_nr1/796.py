import string

inFile = open("A-small-attempt0.in", 'r', 0)
fout = open("A_res.in", "w")
line = inFile.readline()
Total = int(string.split(line)[0])

def calc(r,t):
    a = 0
    for i in range(1,1000):
        a = a + (r+i+(i-1))**2 - (r+i-1+(i-1))**2
        if a > t:
            return i-1
        if a == t:
            return i

for T in range(Total):
    line = inFile.readline()
    r = int(string.split(line)[0])
    t = int(string.split(line)[1])
    ans = calc(r,t)

    fout.write("Case #" + str(T+1) + ": " + str(ans) + "\n")
fout.close()
