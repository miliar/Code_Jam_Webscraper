
def solve(pan,f):
    Npan = ""
    d = 0
    c = 0
    j = 0
    while(j < len(pan)):
        if pan[j] == "-":
            d = j
            Npan = pan[0:d]
            if(d+f > len(pan)):
                return "IMPOSSIBLE"
            for i in range(d,f+d):
                if pan[i] == "-":
                    Npan += "+"
                else:
                    Npan += "-"
            Npan += pan[f+d:len(pan)]
            pan = Npan
            c += 1
            j = 0
            continue
        j+=1
    return str(c)


t = int(input())
for m in range(t):
    en = input().split()
    pan = en[0]
    f = int(en[1])
    print("Case #" + str(m + 1) +": " + solve(pan,f))
