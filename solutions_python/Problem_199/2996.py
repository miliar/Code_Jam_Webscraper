def flip(pancakes, start, k):
    for j in range(start, start+k):
        pancakes[j] = '+' if pancakes[j] == '-' else '-'

T = input()

for i in range(int(T)):
    res = "Case #{0}: ".format(i+1)
    pancakes, k = input().split()
    pancakes = list(pancakes)
    k = int(k)
    
    nflips = 0
    lenPck = len(pancakes)
    for j in range(lenPck-k+1):
        if (pancakes[j] == "-"):
            flip(pancakes, j, k)
            nflips += 1
        
    impossible = False
    for j in range(lenPck-k+1, lenPck):
        if (pancakes[j] == "-"):
            impossible = True
            break
        
    if impossible:
        print(res + "IMPOSSIBLE")
    else:
        print(res + str(nflips))
    

    