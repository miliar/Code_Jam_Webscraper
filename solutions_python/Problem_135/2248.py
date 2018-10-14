inp = open('A-small-attempt0.in')
out = open('A-small-attempt0.out', 'w')
T = int(next(inp))
for test in range(T):
    first = int(next(inp)) - 1
    cards = []
    for i in range(4):
        cards.append([int(x) for x in next(inp).split()])
    important = set(cards[first])
    second = int(next(inp)) - 1
    cards2 = []
    for i in range(4):
        cards2.append([int(x) for x in next(inp).split()])
    important &= set(cards2[second])
    if len(important) > 1:
        res = "Bad magician!"
    elif len(important) == 0:
        res = "Volunteer cheated!"
    else:
        res = str(important.pop())
    out.write("Case #" + str(test + 1) + ": " + res + "\n")
out.close()
inp.close()
    
