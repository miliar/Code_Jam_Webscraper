def all_happy(cakes):
    for c in cakes:
        if c == '-':
            return False
    return True
    
def flipper(cakes, k):
    if all_happy(cakes):
        print(0)
        return
    seen = [cakes]
    possible = [cakes]
    flips = 0
    while possible:
        flips += 1
        next = []
        for c in possible:
            for i in range(len(c) - (k-1)):
                flipped = list(c)
                for j in range(i,i+k):
                    flipped[j] = '-' if flipped[j] == '+' else '+'
                if all_happy(flipped):
                    print(flips)
                    return
                if not flipped in seen:
                    next.append(flipped)
                    seen.append(flipped)
        possible = next
    print("IMPOSSIBLE")

t = int(input())

for i in range(1, t + 1):
    print("Case #" + str(i) + ": ", end="")
    inp = input().split(" ")
    flipper(list(inp[0]),int(inp[1]))
        
        

