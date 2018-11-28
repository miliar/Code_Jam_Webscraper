import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = [x for x in lines if len(x) > 0]

T = int(lines[0],10)
for tt, l in enumerate(lines[1:]):
    pancakes = l.split(" ")[0]
    N = int(l.split(" ")[1], 10)
    
    possible = True
    flips = 0
    pancakes = [c for c in pancakes]
    for i in range(len(pancakes)):
        if pancakes[i] == '-':
            if i+N > len(pancakes):
                possible = False
                break
            for j in range(i, i+N):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                elif pancakes[j] == '+':
                    pancakes[j] = '-'
                else:
                    assert False
            flips += 1

    if possible:
        ans = str(flips)
    else:
        ans = "IMPOSSIBLE"
    print ("Case #%d:" % (tt+1)), ans

        

