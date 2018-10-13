def ispal(s):
    return s == s[::-1]

def Solve(a, b):
    i = 1
    fs = 0
    while(i*i < a):
        i+=1
    while (i*i <= b):
        if ispal(str(i*i)) and ispal(str(i)):
            fs += 1
        i += 1
    return fs
    

FIN  = open("cin",  "r")
FOUT = open("cout", "w")

T = int(FIN.readline())

print (T)
for test in range(T):
    a, b = FIN.readline().split()
    a = int(a)
    b = int(b)
    ans = Solve(a, b)
    st = "Case #" + str(test + 1) + ": " + str(ans) + "\n"
    FOUT.write(st);

FOUT.close()


