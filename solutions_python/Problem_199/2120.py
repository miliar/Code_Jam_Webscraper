def flip(pancakes, i, j):
    for k in range(i, j):
        if pancakes[k] == "-":
            pancakes[k] = "+"
        elif pancakes[k] == "+":
            pancakes[k] = "-"
            
def flip_pancake(pancake, k):
    pancakes = list(pancake)
    flips = 0
    for i in range(len(pancake)-k+1):
        if pancakes[i] == "-":
            flip(pancakes, i, i+k)
            flips += 1
    if "-" in pancakes:
        return "IMPOSSIBLE"
    return str(flips)

#print(flip_pancake("---+-++-", 3))
#print(flip_pancake("+++++", 4))
#print(flip_pancake("-+-+-+", 4))

with open('input.txt') as inf:
    with open('output.txt', 'w') as ouf:
        n = int(inf.readline())
        for i in range(1, n+1):
            line, k = inf.readline().strip().split()
            k = int(k)
            ouf.write('Case #'+str(i)+': '+flip_pancake(line, k)+'\n')
