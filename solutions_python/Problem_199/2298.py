file = open("input.in", 'r').readlines()

t = int(file[0])

with open("output.out", 'w') as f:
    for r in range(t):
        p, k = file[r+1].split(" ")
        k = int(k.strip())
        flips = 0
        for i in range(len(p)):
            if p[i] == '-' and i+k <= len(p):
                newP = p[:i]
                for a in p[i:i+k]:
                    if a == '+':
                        newP += '-'
                    else:
                        newP += '+'
                newP += p[i+k:]
                p = newP
                flips += 1
        for a in p:
            if a == '-':
                flips = "IMPOSSIBLE"


        print("Case #"+str(r+1)+": "+str(flips))
        f.write("Case #"+str(r+1)+": "+str(flips)+"\n")
