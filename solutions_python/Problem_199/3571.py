
def flip(S,i,K):    
    flipped = ""
    if K+i-1 < len(S):
        for pancake_side in range(i,K+i):
            if S[pancake_side] == "+":
                flipped += "-"
            else:
                flipped += "+"        
        S = S[:i] + flipped + S[i+K:]
    return S

with open("A-large.in", "r") as f:
    lines = f.readlines()
    T = int(lines[0])
    x = 1
    result = ""
    while (x < T+1):
        y = 0
        S = lines[x].split()[0]
        K = int(lines[x].split()[1])
        
        happy = "+"*len(S)
        print(S, K)

        j = 0
        while (j < len(S)):
            if (S!=happy):
                i = S.find("-")
                S = flip(S,i,K)
                y += 1
            else:
                break
            j += 1
        
        if j == len(S):
            y = "IMPOSSIBLE"
        
        result += "Case #" + str(x) + ": " + str(y) + "\n"
        print(result)
        x+=1

    file = open("output.o","w") 
    file.write(result)
    file.close()
