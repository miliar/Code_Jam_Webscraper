T = int(input())

def fill(Y, X):
    if cake[Y][X+1] != "?":
        return cake[Y][X+1]
    else:
        cake[Y][X+1] = fill(Y, X+1)
        return cake[Y][X+1]

def check():
    for c in range(R):
        if cake[c].count("?") != 0:
            return False
    return True

for x in range(T):
    R, C = map(int, input().split(" "))
    cake = []
    for y in range(R):
        cake.append(list(input()))
    while check() == False:
        #print(cake)
        for i in range(R):
            if cake[i].count("?") == C:
                #print("HERE")
                if i != 0:
                    if cake[i-1].count("?") != C:
                        cake[i] = cake[i-1]
                    elif i != R and cake[i+1].count("?") != C:
                        cake[i] = cake[i+1]
                else:
                    cake[i] = cake[i+1]
            if cake[i].count("?") > 0:
                #print("NEAR")
                for n in range(C):
                    if cake[i][n] == "?":
                        if n == 0:
                            if cake[i].count("?") != C:
                                cake[i][n] = fill(i, n)
                        else:
                            cake[i][n] = cake[i][n-1]
        #print(cake)
    print("Case #" + str(x+1) + ":")
    for row in cake:
        print("".join(row))
    
