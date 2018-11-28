f = open("pancake.in").read().split("\n")[1:-1]
w = open("pancake.out","w")

for r in range(0,len(f)):
    case = f[r].split(" ")
    case[1] = int(case[1])
    case[0] = list(case[0])
    answer = "0"

    flips = 0
    for i in range(0,len(case[0])-int(case[1])+1):
        if(case[0][i] == "-"):
            for j in range(i,i+case[1]):
                if(case[0][j] == "+"):
                    case[0][j] = "-"
                else:
                    case[0][j] = "+"

            flips+=1

    if("-" in case[0]):
        answer = "IMPOSSIBLE"
    else:
        answer = str(flips)
    

    w.write("Case #"+str(r+1)+": "+answer)
    w.write("\n")

w.close()
