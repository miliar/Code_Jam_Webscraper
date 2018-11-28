M = [["1","i","j","k"],["i","-1","k","-j"],["j","-k","-1","i"],["k","j","-i","-1"]]
def func(a):
    if a == "1" or a == "-1":
        return 0
    elif a == "i" or a == "-i":
        return 1
    elif a == "j" or a == "-j":
        return 2
    elif a == "k" or a == "-k":
        return 3

def mult(a,b):
    if a != "-1" and a != "-i" and a != "-j" and a != "-k":
        if b != "-1" and b != "-i" and b != "-j" and b != "-k":
            result =  M[func(a)][func(b)]
        else:
            result = M[func(a)][func(b)]
            result = "-" + result
    else:
        if b != "-1" and b != "-i" and b != "-j" and b != "-k":
            result = M[func(a)][func(b)]
            result = "-" + result
        else:
            result = M[func(a)][func(b)]

    if len(result) == 3:
        result = result[2]
        return result
    else:
        return result    

T = int(input())
m = 1
while m <= T:
    line = [int(y) for y in input().split()]
    L = int(line[0])
    X = int(line[1])
    string = input()
    i = False
    j = False
    k = False
    l = 0
    cont = 0
    result = "1"
    while l < L*X and (i == False or j == False):
        result = mult(result,string[cont])
        if result == "i" and i == False:
            i = True
            result = "1"
        elif result == "j" and i == True and j == False:
            j = True
            result = "1"

        if (cont+1) % L == 0:
            cont = 0
        else:
            cont += 1
        l += 1

    while l < L*X:
        result = mult(result,string[cont])
        if (cont+1) % L == 0:
            cont = 0
        else:
            cont += 1
        l += 1
        
    if result == "k":
        k = True
    else:
        pass
        
    if i == True and j == True and k == True and l ==  L*X:
        print("Case #" + str(m) + ": " + "YES")
    else:
        print("Case #" + str(m) + ": " + "NO")
    m = m+1
