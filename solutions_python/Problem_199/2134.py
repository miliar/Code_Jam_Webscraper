def parse(test):
    answer = []
    grill, width = test.split(" ")
    width = int(width)
    for cake in grill:
        if cake == '-':
            answer.append(False)
        elif cake == '+':
            answer.append(True)
    return (answer, width)



cases = int(input())
lines = []
for i in range(cases):
    grill, width = parse(input())
    #print(grill)
    flipcount = 0
    for j in range(len(grill) - width + 1):
        if grill[j]:
            continue
        else:
            grill[j:j + width] = [not grill[x] for x in range(j, j + width)]
            #print(grill)
            flipcount += 1
    for cake in grill:
        if not cake:
            print("Case #{}: IMPOSSIBLE".format(i + 1))
            break
    else:
        print("Case #{}: {}".format(i + 1, flipcount))
